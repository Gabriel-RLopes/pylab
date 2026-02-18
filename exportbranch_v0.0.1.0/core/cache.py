import json
from pathlib import Path
from config import CACHE_FILE


class CacheManager:
    def __init__(self):
        self.cache_path = Path(CACHE_FILE)
        self.data = self.load()

    def load(self):
        if self.cache_path.exists():
            return json.loads(self.cache_path.read_text())
        return {}
    
    def save(self):
        self.cache_path.write_text(json.dumps(self.data, indent=2))

    def is_unchanged(self, filepath, md5):
        record = self.data.get(str(filepath))
        return record == md5
    
    def update(self, filepath, md5):
        self.data[str(filepath)] = md5

