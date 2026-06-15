import os
import stat
import urllib.request

STOCKFISH_DIR = "engine/stockfish"
STOCKFISH_PATH = os.path.join(STOCKFISH_DIR, "stockfish")

STOCKFISH_URL = "https://github.com/official-stockfish/Stockfish/releases/latest/download/stockfish-ubuntu-x86-64-avx2"

def ensure_stockfish():
    if not os.path.exists(STOCKFISH_PATH):
        os.makedirs(STOCKFISH_DIR, exist_ok=True)

        print("Downloading Stockfish...")

        urllib.request.urlretrieve(STOCKFISH_URL, STOCKFISH_PATH)

        # make executable (important for Linux/Streamlit Cloud)
        os.chmod(STOCKFISH_PATH, os.stat(STOCKFISH_PATH).st_mode | stat.S_IEXEC)

        print("Stockfish downloaded successfully!")

    return STOCKFISH_PATH