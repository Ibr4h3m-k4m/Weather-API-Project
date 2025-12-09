import httpx
from fastapi import HTTPException

from ..utils.api_config import (
    build_city_url,
    build_geo_url,
    DEFAULT_HEADERS,
    HTTP_TIMEOUT
)
from ..models.weather import WeatherResponse


async def fetch_weather_by_city(city: str) -> WeatherResponse:
    url = build_city_url(city)

    try:
        async with httpx.AsyncClient(timeout=HTTP_TIMEOUT, headers=DEFAULT_HEADERS) as client:
            response = await client.get(url)
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Weather service unavailable")

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Unexpected weather API error")

    data = response.json()

    return WeatherResponse(
        city= city,
        temperature=data["main"]["temp"] - 273.15,  # Convert from Kelvin to Celsius
        humidity=data["main"]["humidity"],
        weather=data["weather"][0]["description"]
    )

#This won't work because of the free tier limitations of OpenWeatherMap API
async def fetch_weather_by_geo(lat: float, lon: float) -> WeatherResponse:
    url = build_geo_url(lat, lon)

    try:
        async with httpx.AsyncClient(timeout=HTTP_TIMEOUT, headers=DEFAULT_HEADERS) as client:
            response = await client.get(url)
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Weather service unavailable")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching geolocation weather")

    data = response.json()

    return WeatherResponse(
        city=f"Coordinates {lat},{lon}",
        weather=data["current"]["weather"][0]["description"],
        temperature=data["current"]["temp"],
        humidity=data["current"]["humidity"]
    )