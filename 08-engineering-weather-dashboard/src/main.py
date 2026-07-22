import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=43.6532"
    "&longitude=-79.3832"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

try:
    # Stop waiting if the server does not respond within 10 seconds.
    response = requests.get(url, timeout=10)

    # Displays the raw JSON text returned by the server.
    #print(response.text)

    if response.status_code == 200:
        data = response.json()

        temperature = data["current"]["temperature_2m"]
        humidity = data["current"]["relative_humidity_2m"]
        wind_speed = data["current"]["wind_speed_10m"]
        time = data["current"]["time"]

        temperature_unit = data["current_units"]["temperature_2m"]
        humidity_unit = data["current_units"]["relative_humidity_2m"]
        wind_speed_unit = data["current_units"]["wind_speed_10m"]

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

    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as error:
    # Catches request problems such as no internet, a timeout,
    # or the server being unavailable.
    print(f"Could not connect to the weather service: {error}")