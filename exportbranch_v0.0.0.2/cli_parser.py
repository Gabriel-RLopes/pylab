import argparse

def parse_args():
    parser = argparse.ArgumentParser( description='ExportBranch' )

    parser.add_argument( '-h', '--help', help='help with valid arguments to be presented!')
    parser.add_argument( '-s', '--source', dest='source', nargs='+', required=True, help='After the -s, the folders to be exported must be specified.')
    parser.add_argument( '-d', '--dest', dest='dest', nargs='+', required=True, help='')
    parser.add_argument( '-r', '--reload', dest='reload', action='store_false', help='' )
    parser.add_argument( '--md5', dest='md5', action='store_true', help='' )

    args = parser.parse_args()

    if args.ext:
        args.ext = [
            e.lower if e.startswith('.') else f'{e.lower}'
            for e in args.ext
        ]

    return args

