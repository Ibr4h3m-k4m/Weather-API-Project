from dotenv import load_dotenv
import os
import httpx

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("You must set API_KEY in your .env file!")

CITY_API_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_API_URL = "https://api.openweathermap.org/data/2.5/onecall"

def build_city_url(city: str) -> str:
    return f"{CITY_API_URL}?appid={API_KEY}&q={city}"

#This won't work because of the free tier limitations of OpenWeatherMap API
def build_geo_url(lat: float, lon: float) -> str:
    return f"{GEO_API_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"


DEFAULT_HEADERS = {
    "Accept": "application/json",
    "User-Agent": "weather-proxy-service/1.0"
}

HTTP_TIMEOUT = httpx.Timeout(
    connect=5,
    read=5,
    write=5,
    pool=5
)
