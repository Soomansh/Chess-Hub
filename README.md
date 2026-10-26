# ChessHub♟️  — Vercel edition
![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-TS-blue?logo=typescript&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployment-Vercel-black?logo=vercel)
![Status](https://img.shields.io/badge/Status-Active-success)
![Project](https://img.shields.io/badge/Project-Chess%20Learning%20Platform-forestgreen)
![GitHub](https://img.shields.io/badge/Source-GitHub-181717?logo=github)
![License](https://img.shields.io/badge/License-See%20Repository-lightgrey)

This is a Next.js migration of the original Streamlit ChessHub project. It keeps the original `games.pgn` and `puzzles.json` data and implements the project's major tools in a browser-based interface.

## Overview 

ChessHub is a chess learning platform running on Vercel. 

I created ChessHub to combine multiple aspects of chess into one single website. The project includes tools for learning openings, reviewing games, practicing endgames, and testing chess knowledge and lastly, MAKE CHESS FUN!

I wanted ChessHub to be more than just a move viewer. My goal was to help players understand why moves are played and how positions develop.

AI assistance was used during development for debugging, troubleshooting, and improving parts of the code.

## Features

- Home dashboard and navigation
- Opening Explorer for ten openings
- Opening recommendation quiz
- Guess The Elo using the included PGN dataset
- Board Visualizer with move navigation
- Play vs AI (uses Lichess cached cloud evaluations when available; falls back to a legal move if no cached line is available)
- Chess Review (PGN paste/upload, move navigation, move labels, approximate evaluation-based accuracy, and best-line hints when Lichess has cached analysis)
- Endgame Puzzle Trainer using the included puzzle dataset
- Learn Endgames lessons

---
#Live Demo
- https://chess-hub-nextjs-q6q5vp398-soomansh.vercel.app/
---

# My Journey Building ChessHub

I started ChessHub as a way to make learning chess more interactive and bring everyone together. The project began as an opening recommendation tool, but it grew into a complete chess learning platform.

Throughout development, I worked on chess visualization, PGN processing, game analysis, and databases. Some of the hardest parts were handling chess positions correctl and integrating analysis tools. After having everything working together, making everything work individually, making it all work together was a rollercoaster of errors and problems. 

The biggest lesson I learned was that building a chess application is not just about moving pieces on a board. It requires understanding chess logic, user experience, and how to turn data into something useful for players. This project really represents me as a person and I hope you truly enjoy this! 


<img width="1912" height="916" alt="image" src="https://github.com/user-attachments/assets/c5a0fac3-09dd-4190-996a-448d70f7f544" />

---

---
Guess the Elo pictures:
<img width="1900" height="915" alt="image" src="https://github.com/user-attachments/assets/ae6956a8-742e-415b-8578-e46148509a06" />
---

---
Board Visualizer pictures:
<img width="1882" height="921" alt="image" src="https://github.com/user-attachments/assets/71150f7d-a55d-46ed-9f75-ab94a5e165d3" />
---

---
Chess Review picture:
<img width="1540" height="810" alt="image" src="https://github.com/user-attachments/assets/00a91104-1c39-4e65-b08d-8059ce2fc6b1" />
---

#  What ChessHub Helps Players Learn 

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



## Run locally

Install Node.js 20 or newer. From this folder, run:

```bash
npm install
npm run dev
```

Open http://localhost:3000.

To test the production build:

```bash
npm run build
```

## Deploy to Vercel

1. Push this project folder to a GitHub repository.
2. In Vercel, choose **Add New → Project** and import that repository.
3. Framework preset: **Next.js**.
4. Build command: `npm run build`.
5. Install command: `npm install`.
6. No environment variables are required for the current version.
7. Deploy, then test each tool from the live site.

## Notes / honest limitations

- Lichess Cloud Evaluation is a cache, not a full Stockfish engine service. Some positions have no cached evaluation. Chess Review reports when evaluation data is unavailable rather than pretending a real engine score exists.
- Play vs AI uses a cached best line where available; when no line is available, it makes a legal fallback move. This is not equivalent to running a full-strength Stockfish engine.
- Accuracy is an estimate based on available evaluations and is not an official Chess.com/Lichess accuracy metric.
- This migration preserves the main user-facing tools, but the Streamlit Python source is not executed by Vercel. Review all features and the live deployment before requesting re-certification.

Vercel deployment trigger.

## LICENSE

This project is licensed under the MIT License. See the `LICENSE` file for more information.

