# ♟️ ChessHub

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![python-chess](https://img.shields.io/badge/python--chess-Chess%20Library-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Type](https://img.shields.io/badge/Project-Chess%20Learning%20Platform-black.svg)

## ♟️ Overview ♟️ 

ChessHub is an interactive chess learning platform built with Python and Streamlit but is run on render :D

The goal of ChessHub is to help players improve at every stage of the game by combining opening education, tactical training, endgame practice, game analysis, and Guess The Elo into one platform.

Instead of only showing moves, ChessHub focuses on helping players understand the ideas behind chess: why moves work, how positions develop, and how to improve decision making.

AI assistance was used during development for debugging, troubleshooting, and improving parts of the code.

---

# DEMO :) 

PS: Guess the Elo will take some time to load as it fetches real random games that are often lengthy

https://chess-hub-2o9y.onrender.com/

# Features 👍

## ♟️ Opening Recommendation System

- Personalized opening suggestions based on:
  - Playing style like if your defensive or really offensive.
  - Skill level ranging from complete beginner to an advanced player looking for a opening to up their game.
  - Strategic preferences to find the most ideal opening that will suit you the most. 

- Interactive chessboard visualization.
- Move by move opening exploration to help recognize moves. 
- Explanations of:
  - Opening ideas/ plan after.
  - Strategic plans and tactics that often appear.
  - Strengths and weaknesses of the opening.
  - Typical middlegame transitions and what to expect/ look for. 

<img width="1397" height="888" alt="image" src="https://github.com/user-attachments/assets/e0966681-9b31-40b1-8f61-a6c71f170a66" />

---

## Chess Review 🤔

Analyze completed chess games through PGN files. This allows the user to input any game and get Chess.com style explanations and descriptions.

Features include:

- PGN upload and paste support.
- Move by move review covering every single position/ move. 
- Position visualizations that help the user recognize and fix their mistakes if any in future games. 
- Move classifications:
  - Best moves ⭐⭐⭐
  - Excellent moves ⭐⭐
  - Good moves ⭐
  - Inaccuracies ⁉️
  - Mistakes ❓
  - Blunders ❓❓
- Accuracy estimates that show something similar to a eval bar.
- Evaluation insights.

<img width="1584" height="877" alt="image" src="https://github.com/user-attachments/assets/947f3064-b1ea-4311-a5c2-3c56a7abd98e" />

---

## Guess The Elo (Inspired by GothamChess's GTE videos)

Inspired by the Guess The Elo concept. Link to real GTE --> https://www.youtube.com/show/VLPLBRObSmbZluTLaLzvOwbOyS6SnnyWVyVT?sbp=KgtjbUpOUjNWTmpRTUAB

Features:

- Random chess games from a lichess database that contains thousands of games.
- A UI thats interactive and allows move playback.
- Guess the player's rating range from 5 possible options.
- Compare your prediction with the players actual rating.
- Track accuracy over multiple games and streaks.
- Improve your own chess skills over time as a result of playing GTE.

<img width="1595" height="877" alt="image" src="https://github.com/user-attachments/assets/d478cacd-4b77-4ccb-b233-8ebd1500784e" />


---

## 🔎 Board Visualizer 🔍

Explore chess positions with an interactive board and teach opening moves.

Features:
- Visualize chess positions and be able to understand their purpose.
- Move pieces and explore ideas eventually making your own adaptations of the opening.
- Step through positions and clearly see what is to be expected.
- Understand board patterns and train your brain to recognize early patterns.
- Color flexibility with pieces. Be able to play as both black and white.

<img width="1694" height="882" alt="image" src="https://github.com/user-attachments/assets/e8153493-d98e-4e3e-b4f5-7ce2aa330548" />


---

##  Endgame Puzzles 🧐

Practice important endgame positions and be able to destroy your opponents in endgames quickly.

Features:
- Solve realistic endgame scenarios coming from real games.
- Improve calculation skills and speed. 
- Learn winning techniques.
- Practice common patterns so time doesnt bother you in a real game. 
- Increase your puzzle streak and accuracy.
- Learn tactics and employ them into your game.

<img width="1711" height="874" alt="image" src="https://github.com/user-attachments/assets/1eae4f4d-d332-432f-9a5c-123e0b1d8799" />


---

##  Learn Endgames 📖

Learn essential endgame concepts and how to utilize them in a real game. 

Topics include:
- King and pawn endings/ how to take advantage of this.
- Piece coordination and how to move your king at the right time etc.
- Winning techniques that force a specific move from the opponent.
- Defensive ideas to ensure you don't weaken your own position. 
- Common endgame principles that will ensure you win the endgame.

<img width="1591" height="772" alt="image" src="https://github.com/user-attachments/assets/4a2dba2f-37cc-4714-a123-5b32f2d4f310" />


---

##  Opening Explorer 📚

Discover and learn chess openings and fully understand them inside out. 

Features:
- Move by move explanations
- Strategic ideas behind openings and the purpose of each of the moves. 
- Common plans and weaknesses to utilize in your games.
- Gain deep knowledge about the opening and the moves you should be making.
- Tactics and how to combat them when faced.

<img width="1584" height="839" alt="image" src="https://github.com/user-attachments/assets/9335b8c3-2f79-4876-ae85-f813267797e8" />


---

##  Play Against AI 🤖

Practice chess against an artificial opponent. 

Features:
- AI gameplay that makes moves based on elo and difficulty.
- Position practice that comes with making right decisions in the right time.
- Transformations of positions.
- Improve calculation and decision making while improving your piece coordination and board tracking. 
- Test learned concepts in games.

<img width="985" height="755" alt="image" src="https://github.com/user-attachments/assets/bd6a18d3-cdbe-4282-bcb3-d7c1e324aa0e" />


---

##  Interactive Chess Experience 👀

- Real time chessboard updates and moves.
- Forward and backward move navigation that makes learning and overall user experience flawless.
- SVG board rendering.
- PGN support which makes everything look clean and work in harmony.
- Clean Render/Streamlit interface.


---

#  What ChessHub Helps Players Learn 🧠

ChessHub is designed to help and teach:

- How openings actually develop and transition into a middlegame.
- The purpose behind opening moves and what to do after.
- Center control and piece movement.
- Piece development in the right order. 
- King safety and king activation. 
- Positional planning and tactics often found in games.
- Transition from middlegame to endgame.
- Endgame concepts to easily promote or checkmate your opponent.
- How mistakes affect a position and how to recover from a mistake or blunder. 


---

# ChessHub is Built With 🔧

- Python
- Streamlit
- python-chess
- Chess SVG Rendering
- Lichess Cloud Analysis API
- PGN Databases


---

## LICENSE

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

# Installation of ChessHub 😄

Clone the repository:

```bash
git clone https://github.com/Soomansh/Chess-Hub.git

