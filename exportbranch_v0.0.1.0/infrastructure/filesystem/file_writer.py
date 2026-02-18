import shutil
from pathlib import Path

class FileWriter:

    def copy(self, src: Path, dst: Path):
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
