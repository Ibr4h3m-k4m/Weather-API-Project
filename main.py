from fastapi import FastAPI
from .routes.weather import weather_router

app = FastAPI(title="Weather Proxy API")

app.include_router(weather_router)

@app.get("/")
def root():
    return {"message": "Weather Proxy API is running!"}
