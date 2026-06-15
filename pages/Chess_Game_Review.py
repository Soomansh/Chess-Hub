
# AI ASSISTANCE WAS USED IN WRITING THIS CODE-------------------------------------------------------------------------

"""
Chess Review

Features:
- PGN Paste
- PGN Upload
- Stockfish Analysis
- Eval Bar
- Move Navigation
- Accuracy Estimates
- Move Classification
- Best Move Suggestions
- Principal Variation Display
- Timeline
- Chessboard Rendering
- Custom Styling
"""

import streamlit as st
import chess
import chess.pgn
import chess.engine
import chess.svg
from io import StringIO
import os
import stat
import urllib.request

# ====================================================================
# STOCKFISH SETUP
# ====================================================================

STOCKFISH_DIR = "engine/stockfish"
STOCKFISH_PATH = os.path.join(STOCKFISH_DIR, "stockfish")

# more stable direct release 
STOCKFISH_URL = "https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-x86-64-avx2"

def ensure_stockfish():
    os.makedirs(STOCKFISH_DIR, exist_ok=True)

    if not os.path.exists(STOCKFISH_PATH):
        print("Downloading Stockfish...")

        try:
            req = urllib.request.Request(
                STOCKFISH_URL,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            with urllib.request.urlopen(req) as response, open(STOCKFISH_PATH, "wb") as out_file:
                out_file.write(response.read())

            os.chmod(STOCKFISH_PATH, 0o755)

            print("Stockfish downloaded successfully!")

        except Exception as e:
            raise RuntimeError(f"Stockfish download failed: {e}")

    return STOCKFISH_PATH

# =================================================================================================
# ANALYSIS DATA
# ============================================================================================================

@st.cache_data(show_spinner=False)
def analyze_position(fen, depth=12):

    board = chess.Board(fen)

    info = engine.analyse(
        board,
        chess.engine.Limit(depth=depth)
    )

    score = info["score"].relative.score(
        mate_score=10000
    )

    if score is None:
        score = 0

    pv = []

    if "pv" in info:
        temp = board.copy()

        for mv in info["pv"][:5]:
            try:
                pv.append(temp.san(mv))
                temp.push(mv)
            except:
                break

    best_move = None

    if "pv" in info and len(info["pv"]) > 0:
        best_move = info["pv"][0]

    return score, pv, best_move

# ================================================================================================
# CLASSIFICATION
# ======================================================================================================

def classify(cpl):

    if cpl <= 5:
        return "🟢 BEST", "Perfect engine move."

    if cpl <= 20:
        return "💎 !! EXCELLENT !!", "Nearly perfect continuation."

    if cpl <= 50:
        return "🔵 ! GREAT !", "Strong move improving the position."

    if cpl <= 100:
        return "⚪ GOOD", "Solid move."

    if cpl <= 200:
        return "🟡 ?! INACCURACY ?!", "Small evaluation loss."

    if cpl <= 400:
        return "🟠 ? MISTAKE ?", "Noticeable strategic loss."

    return "🔴 ?? BLUNDER ??", "Major loss of evaluation."

# =====================================================================================================
# EXPLANATIONS
# ====================================================================================================

def long_explanation(tag):

    explanations = {
        "🟢 BEST":
        "BEST! This matches Stockfish's preferred move and keeps maximum pressure.",

        "💎 !! EXCELLENT !!":
        "EXCELLENT! Very close to the engine's first choice.",

        "🔵 ! GREAT !":
        "GREAT! Strong practical move that maintains an advantage.",

        "⚪ GOOD":
        "GOOD! Playable and reasonable.",

        "🟡 ?! INACCURACY ?!":
        "INACCURACY. A stronger continuation was available.",

        "🟠 ? MISTAKE ?":
        "MISTAKE. This move significantly worsened the position.",

        "🔴 ?? BLUNDER ??":
        "BLUNDER! A major tactical or positional opportunity was missed."
    }

    return explanations.get(tag, "")
 

# ===================================================================================================
# LOAD GAME
# ==================================================================================================

def read_game(text):

    game = chess.pgn.read_game(
        StringIO(text)
    )

    return game

# ==================================================================================================
# REVIEW GENERATION
# =======================================================================================

def build_review(game):

    temp = game.board()

    review = []

    white_loss = 0
    black_loss = 0

    for move_index, move in enumerate(
        game.mainline_moves()
    ):

        before_score, pv, best_move = analyze_position(
            temp.fen()
        )

        san = temp.san(move)

        temp.push(move)

        after_score, _, _ = analyze_position(
            temp.fen()
        )

        cpl = abs(after_score - before_score)

        tag, short_reason = classify(cpl)

        if temp.turn == chess.BLACK:
            white_loss += cpl
        else:
            black_loss += cpl

        review.append({
            "move_number": move_index + 1,
            "san": san,
            "tag": tag,
            "cpl": cpl,
            "reason": short_reason,
            "long_reason": long_explanation(tag),
            "fen": temp.fen(),
            "pv": pv
        })

    return review, white_loss, black_loss

# =====================================================================================================================
# ACCURACY
# ===============================================================================================================

def accuracy(loss, count):

    if count == 0:
        return 100

    value = 100 - (loss / count / 10)

    return max(0, min(100, value))

# ===========================================================================================================
# STATE
# =======================================================================================================

if "review" not in st.session_state:
    st.session_state.review = []

if "index" not in st.session_state:
    st.session_state.index = 0

# =========================================================================================================
# HEADER
# =========================================================================================================

st.title("♟️ Chess Review")

uploaded = st.file_uploader(
    "Upload PGN",
    type=["pgn"]
)

pgn_text = st.text_area(
    "Or Paste PGN"
)

# ====================================================================================================
# LOAD
# =============================================================================================================

if st.button("Analyze Game"):

    text = pgn_text

    if uploaded:
        text = uploaded.read().decode()

    game = read_game(text)

    if game is None:
        st.error("Invalid PGN")
        st.stop()

    review, wloss, bloss = build_review(game)

    st.session_state.review = review
    st.session_state.index = 0

    count = max(1, len(review)//2)

    st.session_state.white_acc = accuracy(
        wloss,
        count
    )

    st.session_state.black_acc = accuracy(
        bloss,
        count
    )

# ==============================================================================================================
# MAIN UI :D
# ======================================================================================================

review = st.session_state.review

if review:

    idx = st.session_state.index

    left, right = st.columns([2,1])

    with left:

        if idx == 0:
            board = chess.Board()
        else:
            board = chess.Board(
                review[idx-1]["fen"]
            )

        arrows = []

        try:
            _, _, best_move = analyze_position(
                board.fen()
            )

            if best_move:
                arrows = [
                    (
                        best_move.from_square,
                        best_move.to_square
                    )
                ]
        except:
            pass

        svg = chess.svg.board(
            board=board,
            size=650,
            arrows=arrows
        )

        st.components.v1.html(
            svg,
            height=680
        )

        col1,col2,col3 = st.columns([1,1,1])

        with col1:
            if st.button("⬅ Previous"):
                st.session_state.index = max(
                    0,
                    idx - 1
                )
                st.rerun()

        with col3:
            if st.button("Next ➡"):
                st.session_state.index = min(
                    len(review)-1,
                    idx + 1
                )
                st.rerun()

        if idx < len(review):

            move = review[idx]

            st.markdown(
                f"<div class='big-tag'>{move['tag']}!!!</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"### Move Played: {move['san']}"
            )

            st.markdown(
                f"**Centipawn Loss:** {int(move['cpl'])}"
            )

            st.markdown(
                f"<div class='explain'>{move['long_reason']}</div>",
                unsafe_allow_html=True
            )

            st.markdown("### Best Line")

            st.write(
                " → ".join(move["pv"])
            )

    with right:

        st.subheader("Accuracy")

        st.metric(
            "White",
            f"{st.session_state.white_acc:.1f}%"
        )

        st.metric(
            "Black",
            f"{st.session_state.black_acc:.1f}%"
        )

        st.subheader("Evaluation")

        if idx == 0:
            score = 0
        else:
            score, _, _ = analyze_position(
                review[idx-1]["fen"]
            )

        score = max(
            -1000,
            min(1000, score)
        )

        percent = (score + 1000)/2000

        st.progress(percent)

        st.subheader("Move Timeline")

        for i, move in enumerate(review):

            marker = "----->" if i == idx else ""

            st.write(
                f"{marker} {i+1}. {move['tag']} {move['san']}"
            )

        st.markdown("---")

        if idx < len(review):

            move = review[idx]

            st.subheader("Move Insight")

            st.write(move["reason"])

            st.write(
                f"This move produced roughly "
                f"{int(move['cpl'])} centipawns "
                f"of evaluation swing."
            )

st.caption(
    "Hope you Enjoy :D"
)
