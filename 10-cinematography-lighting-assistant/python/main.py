import serial

from serial_reader import (
    open_arduino_connection,
    read_light_data,
)


def main():
    """
    Connects to the Arduino and displays live light readings.
    """
    try:
        with open_arduino_connection() as connection:
            print(f"Connected using: {connection.port}")
            print("Press Control+C to stop.\n")

            while True:
                try:
                    light_level, condition = read_light_data(
                        connection
                    )

                    print(
                        f"Light level: {light_level:<4} | "
                        f"Condition: {condition}"
                    )

                except ValueError:
                    # Ignore empty or incomplete startup data.
                    continue

    except serial.SerialException as error:
        print(f"Connection error: {error}")

    except KeyboardInterrupt:
        print("\nLighting Assistant stopped.")


if __name__ == "__main__":
    main()