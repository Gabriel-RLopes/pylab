from pathlib import Path
import os

class Settings:
    CACHE_DB = Path(".cache.db")
    CHUNK_SIZE = 1024 * 1024
    WORKERS = os.cpu_count()
