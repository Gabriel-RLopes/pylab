import os
import platform


WINDOWS_RESERVED = {
    'CON', 'PRN', 'AUX', 'NUL',
    *(f'COM{i}' for i in range(1, 10)),
    *(f'LPT{i}' for i in range(1, 10)),
}

def is_reserved_name(filename):
    name = os.path.splitext(filename)[0].upper()

    if platform.system() == 'Windows':
        return name in WINDOWS_RESERVED
    
    if filename in {'.', '..'}:
        return True
    
    return False
