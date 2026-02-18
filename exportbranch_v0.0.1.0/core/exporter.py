import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from config import MAX_WORKERS

from core.worker import process_file
from core.cache import CacheManager
from core.progress import ProgressBar
from core.compiler import CompilerExecutor


class Exporter:

    def __init__(self, sources, destinations, reload_all=False, use_md5=False, compile_command=None):
        self.sources = [Path(s).resolve() for s in sources]
        self.destinations = [Path(d).resolve() for d in destinations]
        self.reload_all = reload_all
        self.use_md5 = use_md5
        self.cache = CacheManager()
        self.compile_command = compile_command

    def collect_tasks(self):
        tasks = []

        for dest in self.destinations:
            for source in self.sources:
                for root, _, files in os.walk(source):
                    root_path = Path(root)
                    relative = root_path.relative_to(source)
                    target_root = dest / relative        
                    target_root.mkdir(parents=True, exist_ok=True)

                    for file in files:
                        src_file = root_path / file
                        dest_file = target_root / file

                        tasks.append(
                            (src_file, dest_file,
                             self.reload_all,
                             self.use_md5,
                             self.cache)
                        )

        return tasks
    
    def run(self):
        tasks = self.collect_tasks()
        progress = ProgressBar(len(tasks))

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            for _ in executor.map(process_file, tasks):
                progress.update()
        
        progress.close()
        self.cache.save()

        if self.compile_command:
            print('\n iniciando compilacao \n')

            compiler = CompilerExecutor(self.compile_command)
            result = compiler.run()

            print(result['stdout'])

            if result['returncode'] != 0:
                print('erro na compilação: ')
                print(result['stderr'])
                raise RuntimeError('compilacao Falhou')
            else:
                print('compilação finalizada com sucesso.')