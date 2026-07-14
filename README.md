♟️ ChessHub

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![python-chess](https://img.shields.io/badge/python--chess-Engine-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Type](https://img.shields.io/badge/Project-Chess%20Trainer-black.svg)
![Level](https://img.shields.io/badge/Level-Beginner%20Friendly-brightgreen.svg)

A Streamlit based interactive chess application that helps players explore, understand, and choose chess openings based on their playing style, skill level, and strategic preferences.

This project goes beyond simple recommendations by visually demonstrating openings and allowing users to step through moves to better understand how positions develop into the middlegame.

Current Features:

        -Opening recommendations based on player style and skill level

        -Interactive chessboard with move-by-move visualization

        -Step-through navigation (forward and backward through openings)

        -Structured opening database with strategic explanations

        -Educational insights: plans, ideas, strengths, and weaknesses

        -Real-time board updates 

        -Chess Review features that breaks down your games 

        -Guess the Elo: A adapted version inspired by GTE from GothamChess

        -Clean Streamlit UI for simple and fast interaction


This app is designed to help players understand:

        -How chess openings actually develop

        -Why certain moves are played and teaching users the meaning of each move not just memorization

        -Common strategic plans in different openings

        -Transition from opening and into a strong early middlegame

        -Positional ideas like center control, development, and king safety

        -How to win in a Endgame


This project was built with:
        -Python

        -Streamlit

        -python-chess

        -Chess SVG rendering


How to Run:

NOTICE: app.py is now renamed to Opening_Quiz.py!!!

pip install streamlit python-chess

streamlit run app.py

Clone Repo:

        git clone https://github.com/yourusername/chess-trainer.git

        cd chess-trainer
        
Additionally install all other dependencies --> pip install streamlit chess

------------------------------------------------------------------------------------------------------------------------------------------------------------------
IMPORTANT NOTE ABOUT STOCKFISH: 
This project provides both functional frontend and backend components. However, a full Chess.com-style Stockfish engine integration is not included by default. Users are free to extend the project by adding their own engine-based analysis or gameplay features.
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Stockfish Setup and How to Run

Download python from: https://www.python.org/.

        Open a terminal in your project folder and run:

                pip install streamlit chess flask flask-cors

        If you are only using Streamlit, you can skip Flask packages.

        Download Stockfish from the official website: https://stockfishchess.org/download/

        Extract the files
        Locate the executable file (for example: stockfish.exe)
        Move it to a known folder (recommended: inside your project folder)

                Example path:

                C:\Chess\stockfish\stockfish.exe
                

        Open your Python file and set the correct path:

        STOCKFISH_PATH = "stockfish.exe"

        STOCKFISH_PATH = "C:\\Chess\\stockfish\\stockfish.exe"


        In your terminal, run:

                streamlit run app.py

        Then open the local URL shown in the terminal, usually:

                http://localhost:8501

        If your project includes the API backend, run:

                python app.py

        The server will start at:

                http://127.0.0.1:5000



Main Purpose/Objective:

This project was created for a hackathon to combine chess education with interactive visualization. The goal is to make learning openings more fun/effective by showing how positions evolve rather than just listing moves.

Future Improvements to Look Out For:

        -Chess.com style move arrows and analysis lines

        -Engine evaluation bar with the assistance of Stockfish

        -Animated moves

