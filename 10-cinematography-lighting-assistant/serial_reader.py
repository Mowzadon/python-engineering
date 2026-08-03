import time

import serial


PORT = "/dev/cu.usbmodem101"
BAUD_RATE = 9600


def read_light_data():
    """
    Reads and displays live light measurements sent by the Arduino.
    """
    with serial.Serial(PORT, BAUD_RATE, timeout=2) as connection:
        # The Uno usually resets when a serial connection opens.
        time.sleep(2)

        print("Connected to Arduino.")
        print("Press Control+C to stop.\n")

        while True:
            raw_line = connection.readline()

            if not raw_line:
                continue

            line = raw_line.decode("utf-8").strip()

            try:
                light_text, condition = line.split(",", maxsplit=1)
                light_level = int(light_text)

                print(
                    f"Light level: {light_level:<4} | "
                    f"Condition: {condition}"
                )

            except (ValueError, UnicodeDecodeError):
                print(f"Ignored invalid data: {raw_line!r}")


if __name__ == "__main__":
    try:
        read_light_data()

    except serial.SerialException as error:
        print(f"Could not connect to the Arduino: {error}")

    except KeyboardInterrupt:
        print("\nSerial reader stopped.")