from fastapi import FastAPI
from routes.population_routes import router  # Corrected import

app = FastAPI()

# Include the router from continent_routes.py
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)