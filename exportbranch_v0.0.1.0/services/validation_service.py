from pathlib import Path

class ValidationService:

    def __init__(self, allowed_ext=None):
        self.allowed_ext = allowed_ext or []

    def is_valid(self, path: Path) -> bool:
        if not self.allowed_ext:
            return True
        return path.suffix.lower() in self.allowed_ext
