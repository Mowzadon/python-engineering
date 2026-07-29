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