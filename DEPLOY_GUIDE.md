# Beginner-friendly migration and Vercel deployment

## What changed

This is a Next.js version of ChessHub. Vercel can detect the `app/` directory and `next` dependency, so it will no longer look for a Python entry point such as `app.py`. The original PGN and puzzle data are included in `public/data/`.

## 1. Download and extract

Download `ChessHub-Vercel.zip` and extract it. You should see `package.json`, `app/`, `components/`, `public/`, `tsconfig.json`, and `vercel.json` directly inside the extracted folder.

## 2. Make a safe branch on GitHub

1. Open https://github.com/Soomansh/Chess-Hub.
2. Create a new branch named `vercel-migration` from the current default branch. Keep the old code on the original branch as a backup.
3. Clone the repository to your computer, or open your existing local clone.

## 3. Replace the old Streamlit app files

Copy everything inside the extracted `ChessHub-Vercel` folder into the root of your local `Chess-Hub` clone, allowing files to be overwritten.

The new version should be at the repository root. Remove these old Streamlit-only files/folders from the migration branch so the repository is not ambiguous:

- `Home.py`
- `pages/` (the old Python pages)
- `archive_versions/`
- `engine/`
- `data/` (the old data folder; the new data is under `public/data/`)
- `requirements.txt`
- `convert_puzzles.py`
- `extract_puzzles.py`
- `stockfish`
- `stockfish backend`
- `stockfish css`
- `stockfish frontend`
- `stockfish_loader.py`
- the old `package-lock.json` (it was created for the previous dependency set; let npm/Vercel generate a matching lockfile)

Do not delete `public/data/games.pgn` or `public/data/puzzles.json` from the new project.

## 4. Commit and push

Open a terminal in the local repository folder and run:

```bash
git add -A
git commit -m "Migrate ChessHub to Next.js for Vercel"
git push origin vercel-migration
```

If Git says there is nothing to commit, check that the new files were copied into the repository root and that the old files were removed on the migration branch.

## 5. Import into Vercel

1. Open https://vercel.com/new and sign in with GitHub.
2. Import `Soomansh/Chess-Hub`.
3. Select the `vercel-migration` branch for the first deployment.
4. Framework Preset should show **Next.js**. If it shows Python or Other, check that `package.json`, `app/page.tsx`, and `vercel.json` are in the repository root, not inside an extra nested folder.
5. Use the default Root Directory (`./`).
6. Build Command: `npm run build`.
7. Install Command: `npm install`.
8. Do not add environment variables for this version.
9. Deploy and open the resulting URL.

## 6. Test before re-certification

Test each item on the live URL:

- Home page and sidebar navigation
- Opening Explorer: select an opening and step through moves
- Opening Quiz: change answers and request recommendations
- Guess The Elo: wait for the PGN dataset to load, step through a game, submit a guess, and load another game
- Board Visualizer: change the opening, colors, and board size
- Play vs AI: make a legal move on the board
- Chess Review: paste a PGN and analyze it; some positions may have no cached Lichess evaluation
- Endgame Puzzles: load a puzzle and submit a UCI move
- Learn Endgames: switch lessons

If these work, merge `vercel-migration` into the default branch or deploy the tested branch as your production deployment. Send Shipwrights the actual working Vercel URL and request re-certification.

## Important feature limitations

Lichess Cloud Evaluation only returns positions already in its cache. It is not a general-purpose engine endpoint. Chess Review marks missing evaluations as unavailable. Play vs AI uses a cached continuation where available and otherwise makes a legal fallback move; it is not equivalent to a full Stockfish engine. Accuracy figures are estimates, not official chess-platform accuracy scores.
