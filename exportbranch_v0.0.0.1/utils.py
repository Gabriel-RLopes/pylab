import hashlib
import unicodedata
import re
from pathlib import Path
import os


INVALID_WINDOWS_CHARS = r'[<>:"/\\|?*]'
WINDOWS_RESERVED_NAMES = {
    'CON', 'PRN', 'AUX', 'NUL',
    'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
    'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
}


def calc_md5(path, block_size=65536):
    md5 =hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def files_changed(src: Path, dst: Path, use_md5=False):
    if not dst.exists():
        return True
    
    if src.stat().st_size != dst.stat().st_size:
        return True
    
    if int( src.stat().st_mtime ) != int( dst.stat().st_mtime ):
        return True
    
    if use_md5:
        return calc_md5(src) == calc_md5(dst)
    
    return False


def remove_accents( text: str )->str:
    normalized = unicodedata.normalize( 'NFKD', text )
    return ''.join( c for c in normalized if not unicodedata.combining( c ) )


def sanitize_filename( name: str,
                       remove_accent=False,
                       force_Lower=False,
                       replace_space=True ):
    
    base, ext = os.path.splitext( name )

    if remove_accent:
        base = remove_accents( base )

    base = re.sub( INVALID_WINDOWS_CHARS, '', base )

    if replace_space:
        base = base.replace( ' ', '_' )

    base = re.sub(r'_+', '_', base)
    
    if force_Lower:
        base = base.lower()
        ext = ext.lower()

    if base.upper() in WINDOWS_RESERVED_NAMES:
        base=f'{base}_file'

    full = base + ext
    if len( full ) > 255:
        full = full[ :255 ]

    return full
    