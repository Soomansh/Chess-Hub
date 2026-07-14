import streamlit as st
import chess
import chess.svg 

st.title("♟️ Chess Opening")
 
# ===============================================================================================
# BOARD SETTINGS
# ========================================================================================== 

st.sidebar.header("Board Settings")

light_square = st.sidebar.color_picker(
    "Light Squares",
    "#f0d9b5"
)

dark_square = st.sidebar.color_picker(
    "Dark Squares",
    "#b58863"
)

board_size = st.sidebar.slider(
    "Board Size",
    min_value=300,
    max_value=800,
    value=520,
    step=20
    
)

# ====================================================================================================
# OPENINGS (can modify based on preferance)
# =================================================================================================

openings = {
    "Italian Game": [
        "e4", "e5",
        "Nf3", "Nc6",
        "Bc4", "Bc5",
        "c3", "Nf6",
        "d4", "exd4",
        "cxd4", "Bb4+",
        "Nc3"
    ],

    "Queen's Gambit": [
        "d4", "d5",
        "c4", "e6",
        "Nc3", "Nf6",
        "Bg5", "Be7",
        "e3", "O-O",
        "Nf3", "h6",
        "Bh4", "c5"
    ],

    "London System": [
        "d4", "d5",
        "Bf4", "Nf6",
        "e3", "c5",
        "c3", "Nc6",
        "Nd2", "Qb6",
        "Qb3", "c4",
        "Qc2"
    ],

    "Vienna Game": [
        "e4", "e5",
        "Nc3", "Nf6",
        "f4", "d5",
        "fxe5", "Nxe4",
        "Nf3", "Nc6",
        "d4"
    ],

    "Scotch Game": [
        "e4", "e5",
        "Nf3", "Nc6",
        "d4", "exd4",
        "Nxd4", "Bc5",
        "Be3", "Qf6",
        "c3", "Nge7",
        "Bc4"
    ],

    "Sicilian Defense": [
        "e4", "c5",
        "Nf3", "d6",
        "d4", "cxd4",
        "Nxd4", "Nf6",
        "Nc3", "a6",
        "Be3", "e5",
        "Nb3"
    ],

    "Caro-Kann Defense": [
        "e4", "c6",
        "d4", "d5",
        "Nc3", "dxe4",
        "Nxe4", "Bf5",
        "Ng3", "Bg6",
        "h4", "h6"
    ],

    "French Defense": [
        "e4", "e6",
        "d4", "d5",
        "Nc3", "Nf6",
        "Bg5", "Be7",
        "e5", "Nfd7",
        "Bxe7", "Qxe7",
        "f4"
    ],

    "King's Indian Defense": [
        "d4", "Nf6",
        "c4", "g6",
        "Nc3", "Bg7",
        "e4", "d6",
        "Nf3", "O-O",
        "Be2", "e5",
        "O-O", "Nc6"
    ],

    "Pirc Defense": [
        "e4", "d6",
        "d4", "Nf6",
        "Nc3", "g6",
        "Nf3", "Bg7",
        "Be2", "O-O",
        "O-O", "Nc6"
    ]
}

# ================================================================================================
# STATE ITS IN
# ==========================================================================================================

if "step" not in st.session_state:
    st.session_state.step = 0

if "board" not in st.session_state:
    st.session_state.board = chess.Board()

if "current" not in st.session_state:
    st.session_state.current = None

# =====================================================================================================
# SELECT OPENING
# ==============================================================================================

opening = st.selectbox("Choose Opening", list(openings.keys()))
moves = openings[opening]

# reset if changed
if st.session_state.current != opening:
    st.session_state.current = opening
    st.session_state.step = 0
    st.session_state.board = chess.Board()

# ========================================================================================================
# REBUILD BOARD FUNCTION
# ==========================================================================================

def rebuild_board(step):
    board = chess.Board()
    for i in range(step):
        board.push_san(moves[i])
    return board

# ===========================================================================================================
# CONTROLS
# ===================================================================================================

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Back"):
        st.session_state.step = max(0, st.session_state.step - 1)
        st.session_state.board = rebuild_board(st.session_state.step)

with col2:
    if st.button("Next ➡"):
        if st.session_state.step < len(moves):
            st.session_state.board.push_san(moves[st.session_state.step])
            st.session_state.step += 1

# =================================================================================================================
# BOARD RENDERING
# ============================================================================================================

import chess.svg

st.subheader("Board View")

# get last move safely
last_move = None
if len(st.session_state.board.move_stack) > 0:
    last_move = st.session_state.board.peek()

# generate svg board
svg = chess.svg.board(
    board=st.session_state.board,
    size=board_size,
    lastmove=last_move,
    coordinates=True,
    colors={
        "square light": light_square,
        "square dark": dark_square
    }
)

st.markdown(svg, unsafe_allow_html=True)

# ========================================================================================================
# ADDS
# =========================================================================================================

st.write(f"Move: {st.session_state.step} / {len(moves)}")
