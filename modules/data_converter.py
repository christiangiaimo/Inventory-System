import pandas as pd
import os



path = "/home/cgiaimo/Desktop/workspace/github.com/christiangiaimo/Inventory-System/data"
name_file='inventory_data.json'
full_path = os.path.join(path,name_file)

def data_to_json(df):   
    df.to_json(full_path, orient ='records', indent = 4)


def import_data():
    df = pd.read_json(full_path)
    return df
