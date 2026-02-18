import shutil
from utils.hashing import calculate_md5
from utils.fileutils import is_reserved_name


def process_file(task):
    src, dest, reload_all, use_md5, cache = task

    if is_reserved_name(dest.name):
        return

    if dest.exists() and not reload_all:
        if use_md5:
            md5 = calculate_md5(src)
            if cache.is_unchanged(dest, md5):
                return
            
    shutil.copy2(src, dest)

    if use_md5:
        md5 = calculate_md5(dest)
        cache.update(dest, md5)
