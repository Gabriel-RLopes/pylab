from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass(frozen=True)
class FileMetadata:
    path: Path
    size: int
    mtime: float
    md5: Optional[str] = None

