from assigment_1 import read_json 
import os
from pathlib import Path

def main(folder_path):
    folder_name = os.path.basename(folder_path)
    df = read_json.read_folder(folder_path=folder_path)
    df.to_csv(f'{folder_name}.csv', index=None)


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = '\Users\Admin\Downloads\properties'
    abs_file_path = os.path.join(script_dir, rel_path)
    print(abs_file_path)
    
    

