import sqlite3
from pathlib import Path
from core.interfaces import ICache
from core.models import FileMetadata

class SQLiteCache(ICache):

    def __init__(self, db_path: Path):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS files (
            path TEXT PRIMARY KEY,
            size INTEGER,
            mtime REAL,
            md5 TEXT
        )
        """)

    def get(self, path: Path):
        cur = self.conn.execute(
            "SELECT size, mtime, md5 FROM files WHERE path=?",
            (str(path),)
        )
        row = cur.fetchone()
        if not row:
            return None
        return FileMetadata(path, row[0], row[1], row[2])

    def set(self, metadata: FileMetadata):
        self.conn.execute(
            "REPLACE INTO files VALUES (?, ?, ?, ?)",
            (str(metadata.path), metadata.size, metadata.mtime, metadata.md5)
        )
        self.conn.commit()
