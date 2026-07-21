import requests

url = ("https://api.open-meteo.com/v1/forecast"
       "?latitude=43.6532"
       "&longitude=-79.3832"
       "&current=temperature_2m")
try:
    response = requests.get(url, timeout=10) #timeout after waiting for the server for 10 seconds
#print(response) entire response object - displays status code
#print(response.text) #JSON paintext data

    if response.status_code == 200:
        data = response.json()

        temperature = data["current"]["temperature_2m"]
        time = data["current"]["time"]

        print(f"Current temperature: {temperature}°C")
        print(f"Observation time: {time}")

    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as error: #catches request prbolems (i.e. no internet connection, server unavailable, timeout)
    print(f"Could not connect to the weather service: {error}") #error is stored in error