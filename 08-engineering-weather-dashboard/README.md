# Engineering Weather Dashboard

A Python weather dashboard that retrieves current weather and 7-day forecast data from the Open-Meteo API.

The program displays weather information in the terminal, saves weather observations to a CSV file, and generates forecast graphs using Matplotlib.

## Features

- Retrieve current weather data
- Display temperature, humidity, and wind speed
- Display a 7-day weather forecast
- Save weather observations to a CSV file
- Generate and save forecast graphs
- Support multiple Canadian cities
- Handle invalid city input and connection errors

## Supported Cities

- Toronto
- Vancouver
- Calgary
- Montreal

## Project Structure

```text
08-engineering-weather-dashboard/
├── src/
│   ├── main.py
│   ├── api.py
│   ├── weather.py
│   ├── display.py
│   ├── storage.py
│   └── graphs.py
├── data/
│   └── weather_history.csv
├── graphs/
│   └── city_forecast.png
├── requirements.txt
├── README.md
└── .gitignore