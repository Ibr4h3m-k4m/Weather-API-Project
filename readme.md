# Weather Proxy API

A FastAPI-based weather proxy service that fetches weather data from the OpenWeatherMap API and provides a clean, simple interface to retrieve weather information by city name or geographic coordinates.

## Overview

This project serves as a middleware between client applications and the OpenWeatherMap API. It provides a lightweight proxy service that simplifies weather data retrieval with proper error handling and response formatting.

## Features

- ✅ Fetch weather by city name
- ✅ Fetch weather by geographic coordinates (latitude/longitude)
- ✅ Async API endpoints for high performance
- ✅ Error handling with proper HTTP status codes
- ✅ Temperature conversion (Kelvin to Celsius)
- ✅ Structured JSON responses using Pydantic models

## Project Structure
├── main.py # FastAPI application entry point
├── requirements.txt # Python dependencies
├── .env # Environment variables (create your own)
├── models/
│ └── weather.py # Pydantic models for API responses
├── routes/
│ └── weather.py # API route handlers
├── services/
│ └── weather_client.py # OpenWeatherMap API client
└── utils/
└── api_config.py # Configuration and API URL builders

## Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key (free tier available at [openweathermap.org](https://openweathermap.org))

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd weather_proxy-open-weather-API

2. **Create a virtual environment:**


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Create a virtual environment:**
pip install -r requirements.txt
4. **Create a .env file in the root directory:**
API_KEY=your_openweathermap_api_key_here

Usage
Running the Server

uvicorn main:app --reload

The API will be available at http://localhost:8000

API Endpoints
1. Get Weather by City Name
Request:
GET /weather/{city}
Example:

curl http://localhost:8000/weather/London

{
  "city": "London",
  "weather": "overcast clouds",
  "temperature": 8.5,
  "humidity": 72
}


2. Get Weather by Coordinates
Request:
GET /weather/geo/{lat}/{lon}

curl http://localhost:8000/weather/geo/51.5074/-0.1278

Note: This endpoint has limitations due to the free tier of the OpenWeatherMap API.




Dependencies
FastAPI - Modern Python web framework for building APIs
Uvicorn - ASGI server for running FastAPI applications
httpx - Async HTTP client for making API requests
python-dotenv - Environment variable management
Error Handling
The API implements proper error handling with meaningful HTTP status codes:

200 OK - Successful request
404 Not Found - City not found
503 Service Unavailable - Weather service unavailable
500 Internal Server Error - Unexpected API error
API Documentation
Once the server is running, you can access:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
Known Limitations
The geographic coordinates endpoint (/weather/geo/{lat}/{lon}) may not work due to free tier API limitations of OpenWeatherMap
Some features may require a paid OpenWeatherMap subscription
Development
Project Architecture
Models (models) - Pydantic models for request/response validation
Routes (routes) - API endpoint definitions
Services (services) - Business logic and API client implementations
Utils (utils) - Configuration and helper functions
Future Improvements
Add caching to reduce API calls
Implement rate limiting
Add support for additional weather data (wind, pressure, etc.)
Add weather alerts and warnings
Multi-language support
License
This project is open source and available under the MIT License.

Support
For issues or questions, please open an issue in the repository.

Author
Ibr4h3m-k4m

Last Updated: December 2025


Copy the code above and paste it into your `readme.md` file. The formatting is complete and ready to use!Copy the code above and paste it into your `readme.md` file. The formatting is complete and ready to use!
Claude Haiku 4.5 • 1x



Copy the code above and paste it into your `readme.md` file. The formatting is complete and ready to use!Copy the code above and paste it into your `readme.md` file. The formatting is complete and ready to use!
