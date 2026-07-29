def display_weather_dashboard(
    city,
    temperature,
    humidity,
    wind_speed,
    time,
    temperature_unit,
    humidity_unit,
    wind_speed_unit,
):
    """
    Displays the current weather information in a formatted dashboard.

    Args:
        city (str):
            Name of the selected city.

        temperature (float):
            Current air temperature.

        humidity (int):
            Current relative humidity.

        wind_speed (float):
            Current wind speed.

        time (str):
            Observation time.

        temperature_unit (str):
            Unit for temperature.

        humidity_unit (str):
            Unit for humidity.

        wind_speed_unit (str):
            Unit for wind speed.
    """
    label_width = 12

    print("=" * 40)
    print(f"{city} Weather Dashboard")
    print("=" * 40)
    print()

    print(
        f"{'Temperature':<{label_width}}: "
        f"{temperature} {temperature_unit}"
    )
    print(
        f"{'Humidity':<{label_width}}: "
        f"{humidity} {humidity_unit}"
    )
    print(
        f"{'Wind speed':<{label_width}}: "
        f"{wind_speed} {wind_speed_unit}"
    )
    print(f"{'Time':<{label_width}}: {time}")


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
    print("=" * 40)

    for i in range(len(dates)):
        print(
            f"{dates[i]}: "
            f"High {highs[i]} {temperature_unit}, "
            f"Low {lows[i]} {temperature_unit}"
        )