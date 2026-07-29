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