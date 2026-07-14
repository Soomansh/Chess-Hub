import streamlit as st
import chess
import chess.svg
import chess.engine
import urllib.request 
import zipfile
import os
import glob

# ==========================================================================================================================
# STOCKFISH SETUP
# =======================================================================================================================

ENGINE_DIR = "engine"

os.makedirs(ENGINE_DIR, exist_ok=True)

zip_file = os.path.join(ENGINE_DIR, "stockfish.zip")

if not os.path.exists(zip_file):
    try:
        url = "https://stockfishchess.org/files/stockfish_16_linux_x64_avx2.zip"
        urllib.request.urlretrieve(url, zip_file)
    except:
        pass

try:
    if os.path.exists(zip_file):
        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(ENGINE_DIR)
except:
    pass

possible = glob.glob(f"{ENGINE_DIR}/**/*stockfish*", recursive=True)

STOCKFISH_PATH = None

for f in possible:
    if os.path.isfile(f):
        try:
            os.chmod(f, 0o755)
        except:
            pass

        STOCKFISH_PATH = f
        break


@st.cache_resource
def load_engine():
    if STOCKFISH_PATH is None:
        return None

    try:
        return chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    except:
        return None


engine = load_engine()

# ===========================================================================================================================
# BOARD
# =========================================================================================================================

if "board" not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

# ===========================================================================================================================
# OPENINGS
# ====================================================================================================================

openings = {
    "Italian Game": ["e4","e5","Nf3","Nc6","Bc4","Bc5"],
    "Queen's Gambit": ["d4","d5","c4","e6"],
    "London System": ["d4","d5","Bf4","Nf6","e3"],
    "Sicilian Defense": ["e4","c5","Nf3","d6"],
    "French Defense": ["e4","e6","d4","d5"]
}

st.title("♟ Board Trainer")

opening = st.selectbox(
    "Choose Opening",
    list(openings.keys())
)

# ========================================================================================
# CONTROLS(Kinda goofy but trust)
# ==============================================================================================

col1, col2 = st.columns(2)

with col1:
    if st.button("Undo"):
        if board.move_stack:
            board.pop()
        st.rerun()

with col2:
    if st.button("Reset"):
        st.session_state.board = chess.Board()
        st.rerun()

# =========================================================================================================================
# OPENING TRAINER
# ======================================================================================================================

moves = openings[opening]
step = len(board.move_stack)

if step < len(moves):
    st.write(f"Next Move: {moves[step]}")

    if st.button("Play Next Move"):
        try:
            board.push_san(moves[step])
            st.rerun()
        except:
            pass

# =============================================================================================================================
# PLAY MOVE
# ========================================================================================================================

st.subheader("Play Your Move")

move_options = [board.san(m) for m in board.legal_moves]

user_move = st.selectbox(
    "Select move",
    move_options
)

if st.button("Make Move"):

    try:
        board.push_san(user_move)

        if engine:
            result = engine.play(
                board,
                chess.engine.Limit(time=0.2)
            )
            board.push(result.move)

        st.rerun()

    except Exception as e:
        st.error(str(e))

# ==================================================================================================================
# ANALYSIS
# =========================================================================================================

st.subheader("Stockfish Analysis")

level = st.selectbox(
    "Engine Strength",
    ["400","800","1200","1600","2000"]
)

depth_map = {
    "400":1,
    "800":2,
    "1200":5,
    "1600":10,
    "2000":15
}

depth = depth_map[level]


def get_best_move():

    if engine is None:
        return None

    try:
        info = engine.analyse(
            board,
            chess.engine.Limit(depth=depth)
        )

        return info["pv"][0]

    except:
        return None


arrows = []

best = get_best_move()

if best:
    arrows = [
        (best.from_square, best.to_square)
    ]

svg = chess.svg.board(
    board=board,
    size=600,
    arrows=arrows
)

st.components.v1.html(
    svg,
    height=650
)

# ==================================================================================================================
# HISTORY
# ====================================================================================================================

history = []

temp = chess.Board()

for move in board.move_stack:
    try:
        history.append(temp.san(move))
        temp.push(move)
    except Exception:
        break

st.subheader("Move History")

if history:
    st.write(" ".join(history))
else:
    st.write("No moves played yet.")

# =========================================================================================================
# ANALYZE BUTTON
# ===============================================================================================================

if st.button("Analyze Position"):

    best = get_best_move()

    if best:
        st.success(
            f"Best Move: {board.san(best)}"
        )
    else:
        st.warning(
            "Stockfish unavailable"
        )

# ==============================================================================================================
# STATUS
# ========================================================================================================

if board.is_checkmate():
    st.error("Checkmate")

elif board.is_stalemate():
    st.warning("Stalemate")

elif board.is_check():
    st.info("Check")
