import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from config.dependency_container import build_container
from infrastructure.logging.logger import setup_logger

def run_gui():

    setup_logger()
    service = build_container()

    root = tk.Tk()
    root.title("Enterprise Directory Converter")

    def execute():
        source = Path(filedialog.askdirectory())
        destination = Path(filedialog.askdirectory())
        service.convert(source, destination)

    button = tk.Button(root, text="Select and Convert", command=execute)
    button.pack(padx=20, pady=20)

    root.mainloop()
