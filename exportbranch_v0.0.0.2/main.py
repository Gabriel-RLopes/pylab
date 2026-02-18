from cli_parser import parse_args
from core.exporter import Exporter

def main():
    args = parse_args()

    sources = args.souce.split(';')
    destinations = args.destination.split(';')

    exporter = Exporter(
        sources=sources,
        destinations=destinations,
        reload_all=args.reload,
        use_md5=args.md5
    )

    exporter.run()


if __name__ == '__main__':
    main()

