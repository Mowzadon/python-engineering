import requests

def get_weather():
    """
    Retrieves the current weather data from the Open-Meteo API.
        
    Returns: 
        dict | None: 
            A dictionary containing the weather data if the request succeeds, otherwise None. 
    """
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
    print(" Toronto Weather Dashboard")
    print("="*40)
    print()

    print(f"{'Temperature':<{label_width}}: {temperature} {temperature_unit}")
    print(f"{'Humidity':<{label_width}}: {humidity} {humidity_unit}")
    print(f"{'Wind speed':<{label_width}}: {wind_speed} {wind_speed_unit}")
    print(f"{'Time':<{label_width}}: {time}")

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=43.6532"
    "&longitude=-79.3832"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)
def main():

    try:
        data = get_weather()

        if data:
            weather = extract_weather_data(data) 
            #When a function returns comma separated values, Python packs them
            #into a tuple, this unpacks them in the order they were returned. 

            display_weather_dashboard(*weather)# '*' Means take this tuple and unpack it into separate Args. 

        else:
            print(f"Could not retrieve weather data.")

    except requests.exceptions.RequestException as error:
        # Catches request problems such as no internet, a timeout,
        # or the server being unavailable.
        print(f"Could not connect to the weather service: {error}")

if __name__ == "__main__":
    main()