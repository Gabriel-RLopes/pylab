import hashlib
from config import CHUNK_SIZE


def calculate_md5(filepath):
    hash_md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(CHUNK_SIZE):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
