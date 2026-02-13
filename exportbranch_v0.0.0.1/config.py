from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
LOG_DIR = BASE_DIR/'logs'
LOG_DIR.mkdir(exist_ok=True)
