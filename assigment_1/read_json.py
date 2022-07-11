import imp
import csv
from re import I
import pandas as pd
import json
import os

def json_to_list_of_dict(folder_path, file_name):
    """Convert a JSON file to list of dictionary.
    Args:
        folder_path (str): The folder location
        file_name (str) : file name
    Returns:
        List of dictionary
    """
    file = open(os.path.join(folder_path, file_name))
    data = json.load(file)
    return data
    
def folder_to_csv(folder_path):
    """Convert a Folder contains JSON file to csv file.
    Args:
        folder_path (str): The folder location
    Returns:
        CSV file
    """
    to_csv = []
    for file in [file for file in os.listdir(folder_path) if file.endswith(("json"))]:
        data = json_to_list_of_dict(folder_path, file)
        to_csv.append(data)
    
    keys = to_csv[0][0].keys()
    folder_name = os.path.basename(folder_path)

    with open(f'{folder_name}.csv', 'w', encoding='UTF8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = keys)
        writer.writeheader()
        for i in to_csv:
            writer.writerows(i)
            