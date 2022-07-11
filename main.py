from pathlib import Path
from assigment_1 import read_json
import os

def main(folder_path):
    read_json.folder_to_csv(folder_path)

if __name__ == "__main__":
    os.chdir('../properties')
    cwd = Path.cwd()
    main(cwd)
