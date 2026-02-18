import argparse
from pathlib import Path
from config.dependency_container import build_container
from infrastructure.logging.logger import setup_logger
from services.export_service import ExportService

def run():

    parser = argparse.ArgumentParser(description="Enterprise Directory Converter")

    parser.add_argument("source")
    parser.add_argument("destination")
    parser.add_argument("--lower", action="store_true")
    parser.add_argument("--export", action="store_true")

    args = parser.parse_args()

    setup_logger()

    service = build_container()
    service.convert(Path(args.source), Path(args.destination), lower=args.lower)

    if args.export:
        exporter = ExportService()
        exporter.export_zip(Path(args.destination))
