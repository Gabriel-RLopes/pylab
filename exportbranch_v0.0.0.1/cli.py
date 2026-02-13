import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Exportacao'
    )

    parser.add_argument(
        '-s', '--source', dest='source', nargs='+', required=True, help='pasta de origem'
    )

    parser.add_argument(
        '-d', '--dest', dest='dest', nargs='+', required=True, help='pasta de destino'
    )
    
    parser.add_argument(
        '-c', '--ext', dest='ext', nargs='+', help='filtrar por extencoes'
    )
    
    parser.add_argument(
        '-f', '--filter', dest='filter', nargs='+', help='filtrar po nome'
    )
    
    parser.add_argument(
        '--reload', dest='reload', action='store_true', help='reenvia todos os arquivos sem conferencia'
    )
    
    parser.add_argument(
        '--md5', dest='md5', action='store_true', help='calculo md5 na conferencia.'
    )

    parser.add_argument(
        '--lower', dest='lower', action='store_true', help='forca minusculo'
    )

    parser.add_argument(
        '-a', '--no-accent', action='store_true', help='remove acentuacao dos nomes de arquivos'
    )

    args = parser.parse_args()

    if args.ext:
        args.ext = [
            e.lower if e.startswith('.') else f'.{e.lower}'
            for e in args.ext
        ]

    return args
