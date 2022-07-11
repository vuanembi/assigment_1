from assigment_1 import read_json 
import os
from pathlib import Path

def main(folder_path):
    folder_name = os.path.basename(folder_path)
    df = read_json.read_folder(folder_path=folder_path)
    df.to_csv(f'{folder_name}.csv', index=None)


if __name__ == "__main__":
    os.chdir('../properties')
    cwd = Path.cwd()
    main(cwd)
    
    
    

