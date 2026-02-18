from pathlib import Path
from core.interfaces import IFileScanner

class RecursiveScanner(IFileScanner):

    def scan(self, source: Path):
        return (p for p in source.rglob("*") if p.is_file())
