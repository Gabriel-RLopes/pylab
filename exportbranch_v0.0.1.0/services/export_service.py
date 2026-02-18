import shutil
from pathlib import Path

class ExportService:

    def export_zip(self, source: Path, output_name="export"):
        shutil.make_archive(output_name, 'zip', source)
