import streamlit as st
import chess
import chess.pgn
import chess.svg
import random

st.set_page_config(page_title="Guess The Elo", layout="wide")

# =========================================================
# PATH TO YOUR HUGE LICHESS PGN
# =========================================================
PGN_PATH = "data/games.pgn"

# =========================================================
# STREAM RANDOM GAME (NO FULL LOAD)
# =========================================================
@st.cache_data(show_spinner=False)
def get_random_game(sample_size=8000):
    """
    Streams through PGN and randomly selects a good game.
    Does NOT load full file into memory.
    """

    chosen = None
    best_score = -1

    try:
        with open(PGN_PATH, encoding="utf-8", errors="ignore") as pgn:

            for i in range(sample_size):
                game = chess.pgn.read_game(pgn)
                if game is None:
                    break

                moves = list(game.mainline_moves())
                if len(moves) < 10:
                    continue

                try:
                    white_elo = int(game.headers.get("WhiteElo", 0))
                    black_elo = int(game.headers.get("BlackElo", 0))
                except:
                    continue

                avg_elo = (white_elo + black_elo) // 2

                # random selection bias (keeps variety)
                score = random.random()

                if score > best_score:
                    best_score = score

                    chosen = {
                        "moves": moves,
                        "white_elo": white_elo,
                        "black_elo": black_elo,
                        "avg_elo": avg_elo,
                        "opening": game.headers.get("Opening", "Unknown"),
                        "result": game.headers.get("Result", "*"),
                        "event": game.headers.get("Event", "Unknown"),
                        "time_control": game.headers.get("TimeControl", "Unknown"),
                    }

    except Exception as e:
        st.error(f"Error reading PGN: {e}")
        return None

    return chosen


# =========================================================
# ELO BUCKET
# =========================================================
def elo_bucket(elo):
    if elo < 800:
        return "400-800"
    elif elo < 1200:
        return "800-1200"
    elif elo < 1600:
        return "1200-1600"
    elif elo < 2000:
        return "1600-2000"
    return "2000+"


# =========================================================
# TIME CONTROL CLASSIFIER
# =========================================================
def classify_time_control(tc):
    if tc == "Unknown":
        return "Unknown"

    try:
        base = int(tc.split("+")[0])

        if base < 180:
            return "Bullet"
        elif base < 600:
            return "Blitz"
        elif base < 1800:
            return "Rapid"
        else:
            return "Classical"
    except:
        return "Unknown"


# =========================================================
# INIT GAME STATE
# =========================================================
if "game" not in st.session_state:
    st.session_state.game = get_random_game()

if "move_index" not in st.session_state:
    st.session_state.move_index = 0

if "revealed" not in st.session_state:
    st.session_state.revealed = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "questions" not in st.session_state:
    st.session_state.questions = 0


game = st.session_state.game

if not game:
    st.stop()

moves = game["moves"]

board = chess.Board()
for move in moves[:st.session_state.move_index]:
    board.push(move)


# =========================================================
# UI LAYOUT
# =========================================================
left, right = st.columns([2, 1])

with left:
    st.title("♟ Guess The Elo (Streamed Version)")

    svg = chess.svg.board(board=board, size=650)
    st.components.v1.html(svg, height=700)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("<< Start"):
            st.session_state.move_index = 0
            st.rerun()

    with col2:
        if st.button("< Prev"):
            st.session_state.move_index = max(0, st.session_state.move_index - 1)
            st.rerun()

    with col3:
        if st.button("Next >"):
            st.session_state.move_index = min(len(moves), st.session_state.move_index + 1)
            st.rerun()

    with col4:
        if st.button("End >>"):
            st.session_state.move_index = len(moves)
            st.rerun()

    st.write(f"Move: {st.session_state.move_index} / {len(moves)}")

    # ================= MOVE LIST (FIXED) =================
    move_text = []
    temp = chess.Board()

    for i, mv in enumerate(moves):
        try:
            san = temp.san(mv)
            temp.push(mv)

            if i % 2 == 0:
                move_text.append(f"{i//2 + 1}. {san}")
            else:
                move_text[-1] += f" {san}"
        except:
            break

    st.text_area("Moves", " ".join(move_text), height=200)


# =========================================================
# RIGHT PANEL (GUESSING)
# =========================================================
with right:

    st.subheader("Game Info")

    time_type = classify_time_control(game["time_control"])

    st.write("Time Control Type:", time_type)
    st.write("Raw:", game["time_control"])

    guess = st.radio(
        "Guess Elo Range",
        ["400-800", "800-1200", "1200-1600", "1600-2000", "2000+"],
    )

    if st.button("Submit Guess"):
        st.session_state.questions += 1
        st.session_state.revealed = True

        if guess == elo_bucket(game["avg_elo"]):
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error("Incorrect")

    if st.session_state.revealed:
        st.subheader("Results")
        st.write("Actual:", elo_bucket(game["avg_elo"]))
        st.write("Avg Elo:", game["avg_elo"])
        st.write("White:", game["white_elo"])
        st.write("Black:", game["black_elo"])
        st.write("Opening:", game["opening"])
        st.write("Result:", game["result"])
        st.write("Event:", game["event"])

    st.divider()

    acc = 0
    if st.session_state.questions:
        acc = (st.session_state.score / st.session_state.questions) * 100

    st.metric("Score", st.session_state.score)
    st.metric("Questions", st.session_state.questions)
    st.metric("Accuracy", f"{acc:.1f}%")

    if st.button("New Random Game"):
        st.session_state.game = get_random_game()
        st.session_state.move_index = 0
        st.session_state.revealed = False
        st.rerun()
