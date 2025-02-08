from fastapi import APIRouter, HTTPException
import logging
import pandas as pd
from models.continent import read_country_data
from models.validation_population import ContinentPopulationStats

router = APIRouter()

logging.basicConfig(filename="logs/app.log", level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_PATH = "data/world_population.csv"
countries_df = read_country_data(DATA_PATH)
logger.info("✅ Data loaded successfully from CSV.")

def get_continent_countries(continent_name: str):
    filtered_countries = countries_df[countries_df["Continent"].str.lower() == continent_name.lower()]
    if filtered_countries.empty:
        logger.warning(f"⚠️ Continent '{continent_name}' not found.")
        raise HTTPException(status_code=404, detail=f"Continent '{continent_name}' not found.")
    return filtered_countries

@router.get("/continent/{continent_name}", response_model=ContinentPopulationStats)
def get_continent_population_data(continent_name: str):
    try:
        continent_countries = get_continent_countries(continent_name)

        max_pop_country = continent_countries.loc[continent_countries["Population"].idxmax()]
        min_pop_country = continent_countries.loc[continent_countries["Population"].idxmin()]
        avg_population = continent_countries["Population"].mean()
        avg_pop_country = continent_countries.iloc[(continent_countries["Population"] - avg_population).abs().idxmin()]

        return {
            "continent": continent_name,
            "max_population": int(max_pop_country["Population"]),
            "min_population": int(min_pop_country["Population"]),
            "avg_population": round(avg_population, 2),
            "max_population_country": max_pop_country["Country"],
            "min_population_country": min_pop_country["Country"],
            "avg_population_country": avg_pop_country["Country"]
        }
    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
