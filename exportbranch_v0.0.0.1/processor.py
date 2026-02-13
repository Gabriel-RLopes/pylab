import os
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from progress import ProgressBar
from utils import files_changed, sanitize_filename


def collect_files( origins ):
    files = []
    for origin in origins:
        origin = Path( origin ).resolve()
        for root, _, filenames in os.walk( origin ):
            for file in filenames:
                files.append( ( origin / Path( root ) / file ) )


def process_files(origins, destinations, reload_all, use_md5, force_lower, remove_accent=True, max_workers=16):
    
    files = collect_files(origins)
    progress = ProgressBar( len( files ) ) 

    def worker( origin, src ):
        rel = src.relative_to(origin)
        name = sanitize_filename(
            src.name,
            remove_accent=remove_accent,
            force_Lower=force_lower
        )

        for dest in destinations:
            dest = Path(dest).resolve()
            dst = dest /origin.name / rel.parent / name
            dst.parent.mkdir(parents=True, exist_ok=True)
             
            if reload_all or files_changed( src, dst, use_md5 ):
                shutil.copy2(src, dst)

        progress.update()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for origin, src in files:
            executor.submit( worker, origin, src )

    progress.finish()
