from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable
from .models import FileMetadata

class ICache(ABC):

    @abstractmethod
    def get(self, path: Path) -> FileMetadata | None:
        pass

    @abstractmethod
    def set(self, metadata: FileMetadata):
        pass


class IHasher(ABC):

    @abstractmethod
    def hash(self, path: Path) -> str:
        pass


class IFileScanner(ABC):

    @abstractmethod
    def scan(self, source: Path) -> Iterable[Path]:
        pass


class IExecutor(ABC):

    @abstractmethod
    def execute(self, func, items):
        pass
