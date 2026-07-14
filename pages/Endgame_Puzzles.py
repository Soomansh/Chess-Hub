import streamlit as st
import chess
import chess.svg
import chess.engine
import json 
import random

#======================================================================================================
#Connect the stockfish analysis and lichess puzzles database
#========================================================================================================
PUZZLE_PATH = "data/puzzles.json"
STOCKFISH_PATH = "stockfish/stockfish-ubuntu-x86-64-avx2"
#Lichess puzzles database=============================================================================================
@st.cache_data
def load_puzzles():
    with open(PUZZLE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@st.cache_resource
def load_engine():
    try:
        return chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    except:
        return None

all_puzzles = load_puzzles()
engine = load_engine()

#Make sidebar to specify puzzles==========================================================================================
st.sidebar.title("♟ Puzzle Settings")

play_as = st.sidebar.selectbox("Play As", ["Auto", "White", "Black"])

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["All", "Easy", "Medium", "Hard"]
)

mode = st.sidebar.selectbox(
    "Puzzle Type",
    ["All", "Tactics", "Endgame", "Mate"]
)

#Add hints and answer key if feeling stuck on a puzzle=========================================================================
show_hint = st.sidebar.checkbox("Show Hint")
show_answer = st.sidebar.checkbox("Show Solution")

#Sort puzzles based on their elo and skill requirements==================================================================================
def filter_puzzles(puzzles):
    filtered = []

    for p in puzzles:
        rating = int(p.get("rating", 1500))

        themes = " ".join(p.get("themes", [])) if isinstance(p.get("themes"), list) else str(p.get("themes", ""))
        themes = themes.lower()

        if difficulty == "Easy" and rating > 1400:
            continue
        if difficulty == "Medium" and not (1400 <= rating <= 2000):
            continue
        if difficulty == "Hard" and rating < 2000:
            continue

        if mode != "All":
            if mode.lower() not in themes:
                continue

        filtered.append(p)

    return filtered if filtered else puzzles

filtered_puzzles = filter_puzzles(all_puzzles)

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "puzzle" not in st.session_state:
    st.session_state.puzzle = random.choice(filtered_puzzles)

if "board" not in st.session_state:
    st.session_state.board = chess.Board(st.session_state.puzzle["fen"])

if "progress" not in st.session_state:
    st.session_state.progress = 0

if "rating" not in st.session_state:
    st.session_state.rating = 800

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "correct" not in st.session_state:
    st.session_state.correct = 0

if "total" not in st.session_state:
    st.session_state.total = 0

puzzle = st.session_state.puzzle
board = st.session_state.board
#More flexibility to the users======================================================================
solution = puzzle.get("moves", [])
player_color = play_as
if play_as == "Auto":
    player_color = "White" if board.turn else "Black"

st.title("♟ Endgame & Puzzle Trainer")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Puzzle Rating", puzzle.get("rating", "N/A"))

with col2:
    st.metric("Playing As", player_color)

with col3:
    st.metric("Progress", f"{st.session_state.progress}/{len(solution)}")

svg = chess.svg.board(
    board=board,
    size=550,
    orientation=chess.WHITE if player_color == "White" else chess.BLACK
)

st.image(svg)

if show_hint:
    if st.session_state.progress < len(solution):
        st.info(f"Hint: {solution[st.session_state.progress]}")
    elif engine:
        try:
            result = engine.analyse(board, chess.engine.Limit(depth=10))
            st.info(f"Hint: {result['pv'][0].uci()}")
        except:
            pass

if show_answer:
    st.subheader("Solution")
    for i, move in enumerate(solution):
        st.write(f"{i+1}. {move}")

move_text = st.text_input("Your move (UCI format, e.g. e2e4)")

#If the user plays the correct move and basis of the elo system for the actual person =====================================================================
if st.button("Play Move"):
    try:
        move = chess.Move.from_uci(move_text)

        if move not in board.legal_moves:
            st.error("Illegal move")

        else:
            expected = None
            if st.session_state.progress < len(solution):
                expected = solution[st.session_state.progress]

            board.push(move)

            st.session_state.total += 1

            if expected and move.uci() == expected:
                st.success("Correct move")

                st.session_state.correct += 1
                st.session_state.streak += 1
                st.session_state.rating += 10
                st.session_state.progress += 1

                if st.session_state.progress < len(solution):
                    reply = chess.Move.from_uci(solution[st.session_state.progress])

                    if reply in board.legal_moves:
                        board.push(reply)
                        st.info(f"Opponent played: {reply.uci()}")
                        st.session_state.progress += 1

            else:
                st.error("Not the puzzle move")
                st.session_state.streak = 0
                st.session_state.rating -= 5

    except Exception as e:
        st.error(f"Invalid move: {e}")
#Finishing UI=============================================================================================================================
if st.button("Next Puzzle"):
    st.session_state.puzzle = random.choice(filtered_puzzles)
    st.session_state.board = chess.Board(st.session_state.puzzle["fen"])
    st.session_state.progress = 0
    st.rerun()

if st.button("Reset Position"):
    st.session_state.board = chess.Board(st.session_state.puzzle["fen"])
    st.session_state.progress = 0
    st.rerun()

turn_text = "White" if board.turn else "Black"

st.markdown("---")
st.write(f"**Turn:** {turn_text}")
#Accuraccy based on correct answers====================================================================================================
accuracy = 0
if st.session_state.total:
    accuracy = st.session_state.correct / st.session_state.total * 100

st.sidebar.title("Progress")
st.sidebar.metric("Rating", st.session_state.rating)
st.sidebar.metric("Streak", st.session_state.streak)
st.sidebar.metric("Accuracy", f"{accuracy:.1f}%")
st.sidebar.write("Filtered Puzzles:", len(filtered_puzzles))
