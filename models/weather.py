from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    weather: str
    temperature: float
    humidity: int
    weather: str