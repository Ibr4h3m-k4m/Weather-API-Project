from fastapi import APIRouter, Depends

from ..services.weather_client import (
    fetch_weather_by_city,
    fetch_weather_by_geo
)
from ..models.weather import WeatherResponse

weather_router = APIRouter(prefix="/weather", tags=["Weather"])


@weather_router.get("/{city}", response_model=WeatherResponse)
async def get_weather_by_city(city: str):
    return await fetch_weather_by_city(city)

#This won't work because of the free tier limitations of OpenWeatherMap API
@weather_router.get("/geo/{lat}/{lon}", response_model=WeatherResponse)
async def get_weather_by_coordinates(lat: float, lon: float):
    return await fetch_weather_by_geo(lat, lon)
