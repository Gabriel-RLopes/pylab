from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from core.interfaces import IExecutor

class ThreadStrategy(IExecutor):

    def __init__(self, workers):
        self.workers = workers

    def execute(self, func, items):
        items = list(items)
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            list(tqdm(executor.map(func, items), total=len(items), desc="Processing"))
