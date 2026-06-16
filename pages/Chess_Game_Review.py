# AI ASSISTANCE WAS USED IN WRITING THIS CODE-------------------------------------------------------------------------

import streamlit as st
import chess
import chess.pgn
import chess.engine
import chess.svg
from io import StringIO
import os
import urllib.request
import shutil

# ====================================================================
# STOCKFISH SETUP
# ====================================================================

def get_stockfish_path():
    path = shutil.which("stockfish")

    if path is None:
        st.error("Stockfish is not installed on this server.")
        st.stop()

    return path


STOCKFISH_PATH = get_stockfish_path()


@st.cache_resource
def load_engine():
    return chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)


engine = load_engine()

# ====================================================================
# ANALYSIS
# ====================================================================

def analyze_position(engine, fen, depth=12):
    board = chess.Board(fen)

    try:
        info = engine.analyse(board, chess.engine.Limit(depth=depth))
    except:
        return 0, [], None

    score = info["score"].relative.score(mate_score=10000)
    if score is None:
        score = 0

    pv = []
    best_move = None

    if "pv" in info and info["pv"]:
        temp = board.copy()
        for mv in info["pv"][:5]:
            try:
                pv.append(temp.san(mv))
                temp.push(mv)
            except:
                break
        best_move = info["pv"][0]

    return score, pv, best_move


# ====================================================================
# CLASSIFICATION
# ====================================================================

def classify(cpl):
    if cpl <= 5:
        return "🟢 BEST", "Perfect move."
    if cpl <= 20:
        return "💎 EXCELLENT", "Near perfect."
    if cpl <= 50:
        return "🔵 GREAT", "Strong move."
    if cpl <= 100:
        return "⚪ GOOD", "Solid move."
    if cpl <= 200:
        return "🟡 INACCURACY", "Small mistake."
    if cpl <= 400:
        return "🟠 MISTAKE", "Significant loss."
    return "🔴 BLUNDER", "Major error."


def long_explanation(tag):
    return {
        "🟢 BEST": "Perfect engine choice.",
        "💎 EXCELLENT": "Very accurate move.",
        "🔵 GREAT": "Strong continuation.",
        "⚪ GOOD": "Playable move.",
        "🟡 INACCURACY": "Slight inaccuracy.",
        "🟠 MISTAKE": "Clear mistake.",
        "🔴 BLUNDER": "Severe blunder."
    }.get(tag, "")


# ====================================================================
# PGN
# ====================================================================

def read_game(text):
    return chess.pgn.read_game(StringIO(text))


# ====================================================================
# REVIEW ENGINE
# ====================================================================

def build_review(game):
    temp = game.board()
    review = []

    white_loss = 0
    black_loss = 0

    for i, move in enumerate(game.mainline_moves()):

        before_score, pv, best_move = analyze_position(engine, temp.fen())

        san = temp.san(move)
        temp.push(move)

        after_score, _, _ = analyze_position(engine, temp.fen())

        cpl = abs(after_score - before_score)

        tag, reason = classify(cpl)

        if temp.turn == chess.BLACK:
            white_loss += cpl
        else:
            black_loss += cpl

        review.append({
            "san": san,
            "tag": tag,
            "cpl": cpl,
            "reason": reason,
            "long_reason": long_explanation(tag),
            "fen": temp.fen(),
            "pv": pv
        })

    return review, white_loss, black_loss


# ====================================================================
# ACCURACY
# ====================================================================

def accuracy(loss, count):
    if count == 0:
        return 100
    return max(0, min(100, 100 - (loss / count / 10)))


# ====================================================================
# STREAMLIT STATE
# ====================================================================

if "review" not in st.session_state:
    st.session_state.review = []

if "index" not in st.session_state:
    st.session_state.index = 0

if "white_acc" not in st.session_state:
    st.session_state.white_acc = 0

if "black_acc" not in st.session_state:
    st.session_state.black_acc = 0


# ====================================================================
# UI
# ====================================================================

st.title("♟️ Chess Review")

uploaded = st.file_uploader("Upload PGN", type=["pgn"])
pgn_text = st.text_area("Or Paste PGN")


# ====================================================================
# ANALYZE
# ====================================================================

if st.button("Analyze Game"):

    if not pgn_text.strip() and not uploaded:
        st.error("Please upload or paste a PGN.")
        st.stop()

    text = uploaded.read().decode() if uploaded else pgn_text

    game = read_game(text)

    if not game:
        st.error("Invalid PGN")
        st.stop()

    review, wloss, bloss = build_review(game)

    st.session_state.review = review
    st.session_state.index = 0

    count = max(1, len(review) // 2)

    st.session_state.white_acc = accuracy(wloss, count)
    st.session_state.black_acc = accuracy(bloss, count)


# ====================================================================
# DISPLAY
# ====================================================================

review = st.session_state.review

if review:

    idx = st.session_state.index

    left, right = st.columns([2, 1])

    with left:

        board = chess.Board() if idx == 0 else chess.Board(review[idx - 1]["fen"])

        _, _, best_move = analyze_position(engine, board.fen())

        arrows = []
        if best_move:
            arrows = [(best_move.from_square, best_move.to_square)]

        svg = chess.svg.board(board=board, size=650, arrows=arrows)

        st.components.v1.html(svg, height=680)

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("⬅ Previous"):
                st.session_state.index = max(0, idx - 1)
                st.rerun()

        with col3:
            if st.button("Next ➡"):
                st.session_state.index = min(len(review) - 1, idx + 1)
                st.rerun()

        if idx < len(review):
            move = review[idx]

            st.markdown(f"### {move['tag']}")
            st.markdown(f"Move: **{move['san']}**")
            st.markdown(f"CPL: **{int(move['cpl'])}**")
            st.markdown(move["long_reason"])
            st.write(" → ".join(move["pv"]))

    with right:

        st.subheader("Accuracy")
        st.metric("White", f"{st.session_state.white_acc:.1f}%")
        st.metric("Black", f"{st.session_state.black_acc:.1f}%")

        st.subheader("Evaluation")

        if idx == 0:
            score = 0
        else:
            score, _, _ = analyze_position(engine, review[idx - 1]["fen"])

        score = max(-1000, min(1000, score))
        st.progress((score + 1000) / 2000)

        st.subheader("Timeline")

        for i, m in enumerate(review):
            mark = "➡" if i == idx else ""
            st.write(f"{mark} {i+1}. {m['tag']} {m['san']}")

st.caption("Hope you Enjoy :D")
