from infrastructure.cache.sqlite_cache import SQLiteCache
from core.models import FileMetadata
from pathlib import Path

def test_cache_set_get(tmp_path):

    db = tmp_path / "test.db"
    cache = SQLiteCache(db)

    meta = FileMetadata(Path("file.txt"), 10, 1.0, "abc")
    cache.set(meta)

    loaded = cache.get(Path("file.txt"))

    assert loaded.md5 == "abc"
