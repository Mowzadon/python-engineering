import requests
from pathlib import Path
import matplotlib.pyplot as plt

#Dictionary of cities and their corresponding latitude and longitude. 
cities = {
    "Toronto": (43.6532, -79.3832), 
    "Vancouver": (49.2827, -123.1207), 
    "Calgary": (51.0447, -114.0819), 
    "Montreal": (45.5019, -73.5674), 
}


def get_weather(latitude, longitude): #Gives North-South position (horizontal bands around the Earth), Gives East-West position (vertical bands around the Earth).
    """
    Retrieves the current weather data from the Open-Meteo API.
    
    Args: 
        latitude (float):
            Latitude of the location to retrieve weather for.

        longitude (float): 
            Longitude of the location to retrieve weather for.
    
    Returns: 
        dict | None: 
            A dictionary containing the weather data if the request succeeds, otherwise None. 
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=10)

    if response.status_code == 200: 
        return response.json()

    return None 

def extract_weather_data(weather_data):
    """
    Extracts the weather values and their units from the API response. 

    Args: 
        weather_data (dict):
            The JSON dictionary returned by the Open-Meteo API
    
    Returns: 
        tuple: 
            A tuple containing: 
                - temperature
                - humidity
                - wind_speed
                - time
                - temperature_unit
                - humidity_unit
                - wind_speed_unit
    """

    temperature = weather_data["current"]["temperature_2m"]
    humidity = weather_data["current"]["relative_humidity_2m"]
    wind_speed = weather_data["current"]["wind_speed_10m"]
    time = weather_data["current"]["time"]

    temperature_unit = weather_data["current_units"]["temperature_2m"]
    humidity_unit = weather_data["current_units"]["relative_humidity_2m"]
    wind_speed_unit = weather_data["current_units"]["wind_speed_10m"]

    return temperature, humidity, wind_speed, time, temperature_unit, humidity_unit, wind_speed_unit

def display_weather_dashboard(
    city, 
    temperature, 
    humidity, 
    wind_speed, 
    time, 
    temperature_unit, 
    humidity_unit, 
    wind_speed_unit
): 
    """
    Displays the current weather information in a formatted dashboard.

    Args:
        city (str):
            Name of the selected city.

        temperature (float):
            The current air temperature.

        humidity (int):
            The current relative humidity.

        wind_speed (float):
            The current wind speed.

        time (str):
            The observation time.

        temperature_unit (str):
            Unit for temperature.

        humidity_unit (str):
            Unit for humidity.

        wind_speed_unit (str):
            Unit for wind speed.
    """
    # Weather Dashboard
    label_width = 12

    print("="*40)
    print(f"{city} Weather Dashboard")
    print("="*40)
    print()

    print(f"{'Temperature':<{label_width}}: {temperature} {temperature_unit}")
    print(f"{'Humidity':<{label_width}}: {humidity} {humidity_unit}")
    print(f"{'Wind speed':<{label_width}}: {wind_speed} {wind_speed_unit}")
    print(f"{'Time':<{label_width}}: {time}")

def extract_forecast_data(weather_data):
    """
    Args: 
        weather_data (dict):
            The JSON dictionary returned by the Open-Meteo API
    
    Returns: 
        tuple: 
            A tuple containing: 
                - dates (list): 
                    Forecast dates.

                - highs (list):
                    Daily high temperatures.

                - lows (list):
                    Daily low temperatures.
    """
    dates = weather_data["daily"]["time"]
    highs = weather_data["daily"]["temperature_2m_max"]
    lows = weather_data["daily"]["temperature_2m_min"]

    return dates, highs, lows

def display_forecast(dates, highs, lows, temperature_unit): 
    """
    Displays the 7-day weather forecast.

    Args:
        dates (list):
            Forecast dates.

        highs (list):
            Daily high temperatures.

        lows (list):
            Daily low temperatures.

        temperature_unit (str):
            Unit for the temperatures.
    """
    print()
    print("7-Day Forecast")
    print("="*40)

    for i in range(len(dates)): 
        print(
            f"{dates[i]}: "
            f"High {highs[i]} {temperature_unit}, " 
            f"Low {lows[i]} {temperature_unit}"
        )

def save_weather_data(
    city,
    time,
    temperature,
    humidity,
    wind_speed,
):
    """
    Saves the current weather observation to weather_history.csv.

    If the file does not exist, it is created and a header row is written.
    """
    project_folder = Path(__file__).resolve().parent.parent
    data_folder = project_folder / "data"
    data_folder.mkdir(exist_ok=True)

    file_path = data_folder / "weather_history.csv"
    file_exists = file_path.exists()

    with open(file_path, "a", newline="") as file:
        if not file_exists:
            file.write("City,Time,Temperature,Humidity,Wind Speed\n")

        file.write(
            f"{city},{time},{temperature},{humidity},{wind_speed}\n"
        )

def plot_forecast(city, dates, highs, lows):
    """
    Creates, saves, and displays a line graph of the 7-day weather forecast.

    Args:
        city (str):
            Name of the selected city.

        dates (list):
            Forecast dates.

        highs (list):
            Daily high temperatures.

        lows (list):
            Daily low temperatures.
    """
    project_folder = Path(__file__).resolve().parent.parent

    graphs_folder = project_folder / "graphs"
    graphs_folder.mkdir(exist_ok=True)

    graph_path = graphs_folder / f"{city.lower()}_forecast.png"

    plt.figure(figsize=(10, 5))

    plt.plot(dates, highs, label="High")
    plt.plot(dates, lows, label="Low")

    plt.title(f"{city} 7-Day Weather Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()

    plt.savefig(graph_path)
    plt.show()
    plt.close()


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

        if data:
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
            )

            save_weather_data(
                city,
                time,
                temperature,
                humidity,
                wind_speed,
            )

        else:
            print(f"Could not retrieve weather data.")

    except requests.exceptions.RequestException as error:
        # Catches request problems such as no internet, a timeout,
        # or the server being unavailable.
        print(f"Could not connect to the weather service: {error}")

if __name__ == "__main__":
    main()