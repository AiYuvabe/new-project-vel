from pydantic import BaseModel

class ContinentPopulationStats(BaseModel):
    continent: str 
    max_population: int
    min_population: int
    avg_population: float
    max_population_country: str
    min_population_country: str
    avg_population_country: str


# import os
# import sys

# src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..","population"))
# sys.path.append(src_directory)
# from streamlit_app.app import hell


# print(hell())