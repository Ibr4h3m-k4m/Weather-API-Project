# 🌦️ Weather API Proxy

A modern, high-performance weather proxy service built with FastAPI that simplifies access to real-time weather data from OpenWeatherMap API.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Error Handling](#error-handling)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This Weather API Proxy serves as an intelligent middleware layer between your applications and the OpenWeatherMap API. It provides a clean, RESTful interface with automatic temperature conversion, structured responses, and robust error handling.

**Why use this proxy?**
- Simplified API interface with consistent responses
- Built-in error handling and validation
- Automatic temperature conversion (Kelvin → Celsius)
- Async/await support for optimal performance
- Type-safe with Pydantic models
- Auto-generated API documentation

## ✨ Features

- 🌍 **Fetch weather by city name** - Simple queries using city names
- 📍 **Fetch weather by coordinates** - Precise location-based weather data
- ⚡ **Async endpoints** - Non-blocking I/O for high throughput
- 🛡️ **Type safety** - Pydantic models ensure data integrity
- 📊 **Auto documentation** - Interactive Swagger UI and ReDoc
- 🌡️ **Smart conversions** - Automatic Kelvin to Celsius conversion
- 🔒 **Secure configuration** - Environment-based API key management
- 🎯 **Structured responses** - Consistent JSON format across endpoints

## 📁 Project Structure

```
Weather-API-Project/
│
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not in repo)
├── .env.example              # Example environment file
│
├── models/
│   └── weather.py            # Pydantic response models
│
├── routes/
│   └── weather.py            # API route handlers
│
├── services/
│   └── weather_client.py     # OpenWeatherMap API integration
│
└── utils/
    └── api_config.py         # Configuration and helpers
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenWeatherMap API key ([Get one free here](https://openweathermap.org/api))

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ibr4h3m-k4m/Weather-API-Project.git
   cd Weather-API-Project
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your API key
   # API_KEY=your_openweathermap_api_key_here
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory with the following:

```env
API_KEY=your_openweathermap_api_key_here
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

**Important:** Never commit your `.env` file to version control. It's already in `.gitignore`.

## 💻 Usage

### Starting the Server

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

For production:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### API Endpoints

#### 1. Get Weather by City Name

**Endpoint:** `GET /weather/{city}`

**Example:**
```bash
curl http://localhost:8000/weather/London
```

**Response:**
```json
{
  "city": "London",
  "weather": "overcast clouds",
  "temperature": 8.5,
  "humidity": 72
}
```

**Try it:**
```bash
# Different cities
curl http://localhost:8000/weather/Paris
curl http://localhost:8000/weather/Tokyo
curl http://localhost:8000/weather/New%20York  # URL encode spaces
```

#### 2. Get Weather by Geographic Coordinates

**Endpoint:** `GET /weather/geo/{lat}/{lon}`

**Example:**
```bash
# London coordinates
curl http://localhost:8000/weather/geo/51.5074/-0.1278
```

**Response:**
```json
{
  "city": "London",
  "weather": "clear sky",
  "temperature": 12.3,
  "humidity": 65
}
```

**Note:** This endpoint may have limitations on the OpenWeatherMap free tier.

## 📚 API Documentation

Once the server is running, access the interactive documentation:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
  - Interactive API explorer
  - Test endpoints directly in browser
  - View request/response schemas

- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
  - Clean, three-panel documentation
  - Better for reading and sharing

## 🔧 Error Handling

The API provides meaningful error responses with appropriate HTTP status codes:

| Status Code | Description |
|------------|-------------|
| `200 OK` | Request successful |
| `404 Not Found` | City not found or invalid coordinates |
| `503 Service Unavailable` | OpenWeatherMap API unavailable |
| `500 Internal Server Error` | Unexpected error occurred |

**Example Error Response:**
```json
{
  "detail": "City not found"
}
```

## 🛠️ Development

### Running Tests

```bash
# Install development dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### Code Style

This project follows PEP 8 guidelines. Format your code with:

```bash
pip install black
black .
```

### Project Architecture

- **Models Layer** (`models/`) - Pydantic schemas for data validation
- **Routes Layer** (`routes/`) - FastAPI endpoint definitions
- **Services Layer** (`services/`) - Business logic and external API calls
- **Utils Layer** (`utils/`) - Helper functions and configuration

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| FastAPI | Latest | Web framework |
| Uvicorn | Latest | ASGI server |
| httpx | Latest | Async HTTP client |
| python-dotenv | Latest | Environment management |
| Pydantic | Latest | Data validation |

See `requirements.txt` for complete list.

## 🚧 Known Limitations

- Geographic coordinates endpoint may not work consistently with free tier OpenWeatherMap API
- Rate limiting is subject to OpenWeatherMap's free tier restrictions (60 calls/minute)
- Some advanced weather features require paid OpenWeatherMap subscription

## 🗺️ Roadmap

Future enhancements planned:

- [ ] Response caching with Redis
- [ ] Rate limiting middleware
- [ ] Support for 5-day forecast
- [ ] Weather alerts and warnings
- [ ] Wind speed and direction data
- [ ] Air quality index
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Unit and integration tests
- [ ] CI/CD pipeline

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👤 Author

**Ibr4h3m-k4m**

- GitHub: [@Ibr4h3m-k4m](https://github.com/Ibr4h3m-k4m)
- Project Link: [https://github.com/Ibr4h3m-k4m/Weather-API-Project](https://github.com/Ibr4h3m-k4m/Weather-API-Project)


---

**Last Updated:** December 2024

**Status:** Active Development

Made with ❤️ by [Ibr4h3m-k4m](https://github.com/Ibr4h3m-k4m)
