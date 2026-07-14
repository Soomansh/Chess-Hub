import streamlit as st

st.set_page_config(
    page_title="Chess Hub",
    page_icon="♟️",
    layout="wide"
)

# -------------------------------------------------------- HEADER -------------------------------------------------------------
st.title("♟️ Chess Hub")
st.subheader("Learn • Train • Analyze • Improve")

st.markdown("---")

# -------------------------------------- INTRO ---------------------------------------------
st.write("""
Welcome to your chess platform.

Everything is connected here:
- Learn openings in depth
- Practice positions on a board
- Play against Stockfish AI
- Review full games like Chess.com
""")

st.markdown("---")

# ------------------------------------------------- NAVIGATION ------------------------------------------------------------
st.header("Open Tools")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Learning")

    if st.button("Chess Quiz"):
        st.switch_page("pages/Chess_Quiz.py")

    if st.button("Opening Explorer"):
        st.switch_page("pages/Opening_Explorer.py")

    if st.button("Guess the Elo"):
        st.switch_page("pages/Guess_The_Elo.py")

with col2:
    st.subheader("Training & Analysis")

    if st.button("Board Visualizer"):
        st.switch_page("pages/Board_Visualizer.py")

    if st.button("Play vs AI"):
        st.switch_page("pages/Play_Against_Ai.py")

    if st.button("Chess Games Review"):
        st.switch_page("pages/Chess_Game_Review.py")

    if st.button("Endgame Puzzles"):
        st.switch_page("pages/Endgame_Puzzles.py")

    if st.button("Learn Endgames"):
        st.switch_page("pages/Learn_Endgames.py")

st.markdown("---")

# ------------------------------------------------- STATUS -----------------------------------------------------
st.header("What this platform does")

st.info("""
1. Opening learning system
2. Quiz-based training
3. Board practice tools
4. AI opponent 
5. Full game review system
6. Endgame puzzles
7. Endgame tactics learning system
""")

st.markdown("---")

st.caption("♟️ Chess Hub • Python • Streamlit • Stockfish")
