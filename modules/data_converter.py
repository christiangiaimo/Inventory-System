import pandas as pd
import os




def data_to_json(df):   
    df.to_json(full_path, orient ='records', indent = 4)


def import_data():
    df = pd.read_json(full_path)
    return df
