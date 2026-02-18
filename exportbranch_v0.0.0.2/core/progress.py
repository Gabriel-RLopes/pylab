from tqdm import tqdm


class ProgressBar:
    def __init__(self, total):
        self.bar = tqdm(total=total, unit='file')

    def update(self):
        self.bar.update(1)

    def close(self):
        self.bar.close()
