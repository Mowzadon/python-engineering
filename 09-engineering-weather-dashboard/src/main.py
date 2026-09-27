import requests
from api import get_weather
from weather import extract_weather_data, extract_forecast_data
from display import display_weather_dashboard, display_forecast
from storage import save_weather_data
from graphs import plot_forecast


#Dictionary of cities and their corresponding latitude and longitude. 
cities = {
    "Toronto": (43.6532, -79.3832), 
    "Vancouver": (49.2827, -123.1207), 
    "Calgary": (51.0447, -114.0819), 
    "Montreal": (45.5019, -73.5674), 
}

def main():

    try:
        city = input(
            "Please enter the name of a city for the weather forecast: "
            ).strip().title() #.strip() removes leading and trailing whitespaces (or any specified chars), .title() titlecases each word
        if city not in cities: 
            print("That city is not available.")
            return #Exits main so python does not attempt an invalid dictionary lookup.
        
        latitude, longitude= cities[city] #Unpack coordinates since each dictionary value is a tuple. 
        data = get_weather(latitude, longitude)

        if data is not None:
            (
                temperature,
                humidity,
                wind_speed,
                time,
                temperature_unit,
                humidity_unit,
                wind_speed_unit,
            ) = extract_weather_data(data)

            display_weather_dashboard(
                city,
                temperature,
                humidity,
                wind_speed,
                time,
                temperature_unit,
                humidity_unit,
                wind_speed_unit,
            )

            dates, highs, lows = extract_forecast_data(data)

            display_forecast(
                dates,
                highs,
                lows,
                temperature_unit,
            )

            plot_forecast(
                city,
                dates, 
                highs,
                lows,   
                temperature_unit,
            )

            save_weather_data(
                city,
                time,
                temperature,
                humidity,
                wind_speed,
            )

        else:
            print("Could not retrieve weather data.")

    except requests.exceptions.RequestException as error:
        # Catches request problems such as no internet, a timeout,
        # or the server being unavailable.
        print(f"Could not connect to the weather service: {error}")

if __name__ == "__main__":
    main()