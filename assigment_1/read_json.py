import imp
import pandas as pd
import os
def read_json(folder_path, file_name: str) -> pd.DataFrame:
    """Convert a JSON file to pandas object.
    Args:
        folder_path (str): The folder location
        file_name (str) : file name
    Returns:
        DataFrame
    """
    df = pd.read_json(os.path.join(folder_path, file_name))
    return df


def read_folder(folder_path: str) -> pd.DataFrame:
    """Convert folder contains JSON files to pandas object.
    Args:
        folder_path (str): The folder location
    Returns:
        DataFrame
    """
    dfs = []
    for file in os.listdir(folder_path):
        if file.endswith(("json")):
            df = read_json(folder_path, file)
            dfs.append(df)
    return pd.concat(dfs)