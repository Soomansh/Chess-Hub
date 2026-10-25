# ChessHub — Vercel edition

This is a Next.js migration of the original Streamlit ChessHub project. It keeps the original `games.pgn` and `puzzles.json` data and implements the project's major tools in a browser-based interface.

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

Some Pictures:
<img width="1912" height="916" alt="image" src="https://github.com/user-attachments/assets/c5a0fac3-09dd-4190-996a-448d70f7f544" />
<img width="1900" height="915" alt="image" src="https://github.com/user-attachments/assets/ae6956a8-742e-415b-8578-e46148509a06" />
<img width="1882" height="921" alt="image" src="https://github.com/user-attachments/assets/71150f7d-a55d-46ed-9f75-ab94a5e165d3" />






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
