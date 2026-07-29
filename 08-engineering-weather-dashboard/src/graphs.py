from pathlib import Path

import matplotlib.pyplot as plt


def plot_forecast(city, dates, highs, lows, temperature_unit):
    """
    Creates, saves, and displays a line graph of the 7-day forecast.

    Args:
        city (str):
            Name of the selected city.

        dates (list):
            Forecast dates.

        highs (list):
            Daily high temperatures.

        lows (list):
            Daily low temperatures.

        temperature_unit (str):
            Unit used for the forecast temperatures.
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
    plt.ylabel(f"Temperature ({temperature_unit})")
    plt.grid(True)
    plt.legend()

    plt.savefig(graph_path)
    plt.show()
    plt.close()