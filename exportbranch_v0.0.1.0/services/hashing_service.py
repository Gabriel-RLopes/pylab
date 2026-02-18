import hashlib
from pathlib import Path
from core.interfaces import IHasher
from config.settings import Settings

class MD5Hasher(IHasher):

    def hash(self, path: Path) -> str:
        md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(Settings.CHUNK_SIZE), b""):
                md5.update(chunk)
        return md5.hexdigest()
