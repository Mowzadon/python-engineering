import csv
from datetime import datetime
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "data"
DATA_FILE = DATA_FOLDER / "light_history.csv"


def save_reading(light_level, condition):
    """
    Saves one light reading to light_history.csv.

    Args:
        light_level (int):
            Current Arduino light reading.

        condition (str):
            Classified lighting condition.
    """
    DATA_FOLDER.mkdir(exist_ok=True)

    file_exists = DATA_FILE.exists()

    timestamp = datetime.now().isoformat(timespec="seconds")

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Timestamp", "Light Level", "Condition"]
            )

        writer.writerow(
            [timestamp, light_level, condition]
        )