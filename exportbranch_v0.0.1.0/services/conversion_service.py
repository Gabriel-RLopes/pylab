import logging
from pathlib import Path
from core.models import FileMetadata
from core.policies import normalize_filename

class ConversionService:

    def __init__(self, scanner, hasher, cache, writer, executor):
        self.scanner = scanner
        self.hasher = hasher
        self.cache = cache
        self.writer = writer
        self.executor = executor

    def convert(self, source: Path, destination: Path, lower=False):

        files = list(self.scanner.scan(source))

        def task(path: Path):
            md5 = self.hasher.hash(path)
            cached = self.cache.get(path)

            if cached and cached.md5 == md5:
                logging.info(f"SKIPPED: {path}")
                return

            normalized = normalize_filename(path.name, lower)
            target = destination / normalized

            self.writer.copy(path, target)

            metadata = FileMetadata(
                path=path,
                size=path.stat().st_size,
                mtime=path.stat().st_mtime,
                md5=md5
            )

            self.cache.set(metadata)
            logging.info(f"COPIED: {path}")

        self.executor.execute(task, files)
