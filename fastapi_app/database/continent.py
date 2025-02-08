import pandas as pd



# def read_country_data(file_path: str):
#     return pd.read_csv(file_path)

path_world = "c:/Users/velu/Downloads/world_population.csv"

def read_country_data(path_world):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path_world)
    return df
