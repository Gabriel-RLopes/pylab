from infrastructure.cache.sqlite_cache import SQLiteCache
from infrastructure.filesystem.file_scanner import RecursiveScanner
from infrastructure.filesystem.file_writer import FileWriter
from infrastructure.execution.strategies import ThreadStrategy
from services.hashing_service import MD5Hasher
from services.conversion_service import ConversionService
from config.settings import Settings

def build_container():

    cache = SQLiteCache(Settings.CACHE_DB)
    scanner = RecursiveScanner()
    writer = FileWriter()
    hasher = MD5Hasher()
    executor = ThreadStrategy(Settings.WORKERS)

    return ConversionService(
        scanner=scanner,
        hasher=hasher,
        cache=cache,
        writer=writer,
        executor=executor
    )
