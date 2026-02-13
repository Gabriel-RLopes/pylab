from cli import parse_args
from processor import process_files

def main():
    
    args=parse_args()

    process_files(
        origins=args.source,
        destinations=args.dest,
        reload_all=args.reload,
        use_md5=args.md5,
        force_lower=args.lower,
        remove_accent=args.no_accent
    )

if __name__ == '__main__':
    main()
