import requests

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
