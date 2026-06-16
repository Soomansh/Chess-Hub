# AI ASSISTANCE WAS USED IN WRITING THIS CODE-------------------------------------------------------------------------

import streamlit as st
import chess
import chess.pgn
import chess.svg
import requests
from io import StringIO

# =========================
# LICHESS CLOUD ENGINE API
# =========================

LICHESS_API = "https://lichess.org/api/cloud-eval"


def analyze_position(fen):
    """
    Cloud-based chess analysis (NO STOCKFISH NEEDED)
    """
    try:
        r = requests.get(LICHESS_API, params={"fen": fen}, timeout=5)
        data = r.json()

        cp = 0
        pv = []
        best_move = None

        if "pvs" in data and len(data["pvs"]) > 0:
            line = data["pvs"][0]

            cp = line.get("cp", 0)

            if "moves" in line:
                moves = line["moves"].split()
                pv = moves[:5]
                best_move = moves[0] if moves else None

        return cp, pv, best_move

    except:
        return 0, [], None


# =========================
# CLASSIFICATION
# =========================

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


# =========================
# PGN LOADER
# =========================

def read_game(text):
    return chess.pgn.read_game(StringIO(text))


# =========================
# REVIEW ENGINE
# =========================

def build_review(game):
    board = game.board()
    review = []

    white_loss = 0
    black_loss = 0

    for move in game.mainline_moves():

        before_score, pv, best_move = analyze_position(board.fen())

        san = board.san(move)
        board.push(move)

        after_score, _, _ = analyze_position(board.fen())

        cpl = abs(after_score - before_score)

        tag, reason = classify(cpl)

        if board.turn == chess.BLACK:
            white_loss += cpl
        else:
            black_loss += cpl

        review.append({
            "san": san,
            "tag": tag,
            "cpl": cpl,
            "reason": reason,
            "long_reason": long_explanation(tag),
            "fen": board.fen(),
            "pv": pv
        })

    return review, white_loss, black_loss


# =========================
# ACCURACY
# =========================

def accuracy(loss, count):
    if count == 0:
        return 100
    return max(0, min(100, 100 - (loss / count / 10)))


# =========================
# STATE
# =========================

if "review" not in st.session_state:
    st.session_state.review = []

if "index" not in st.session_state:
    st.session_state.index = 0

if "white_acc" not in st.session_state:
    st.session_state.white_acc = 0

if "black_acc" not in st.session_state:
    st.session_state.black_acc = 0


# =========================
# UI
# =========================

st.title("♟️ Chess Review (Cloud Engine Version)")

uploaded = st.file_uploader("Upload PGN", type=["pgn"])
pgn_text = st.text_area("Or Paste PGN")


# =========================
# ANALYZE BUTTON
# =========================

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


# =========================
# DISPLAY
# =========================

review = st.session_state.review

if review:

    idx = st.session_state.index

    left, right = st.columns([2, 1])

    with left:

        board = chess.Board() if idx == 0 else chess.Board(review[idx - 1]["fen"])

        _, _, best_move = analyze_position(board.fen())

        arrows = []
        if best_move:
            try:
                arrows = [(chess.Move.from_uci(best_move).from_square,
                           chess.Move.from_uci(best_move).to_square)]
            except:
                arrows = []

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
            score, _, _ = analyze_position(review[idx - 1]["fen"])

        score = max(-1000, min(1000, score))
        st.progress((score + 1000) / 2000)

        st.subheader("Timeline")

        for i, m in enumerate(review):
            mark = "➡" if i == idx else ""
            st.write(f"{mark} {i+1}. {m['tag']} {m['san']}")

st.caption("Hope you Enjoy :D")
