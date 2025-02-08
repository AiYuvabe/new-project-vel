import pandas as pd

def read_country_data(path_world):
    """Reads CSV data into a Pandas DataFrame"""
    return pd.read_csv(path_world)