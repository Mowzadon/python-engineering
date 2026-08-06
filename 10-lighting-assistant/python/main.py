import serial

from analysis import (
    calculate_statistics,
    recommend_camera_settings,
)
from display import display_dashboard
from graphs import plot_session
from serial_reader import (
    open_arduino_connection,
    read_light_data,
)
from storage import save_reading


def main():
    """
    Runs the Cinematography Lighting Assistant.
    """
    readings = []

    try:
        with open_arduino_connection() as connection:
            print(f"Connected using: {connection.port}")

            while True:
                try:
                    light_level, condition = read_light_data(
                        connection
                    )

                    readings.append(light_level)

                    save_reading(
                        light_level,
                        condition,
                    )

                    (
                        minimum,
                        maximum,
                        average,
                        sample_count,
                    ) = calculate_statistics(readings)

                    recommendation = recommend_camera_settings(
                        condition
                    )

                    display_dashboard(
                        light_level,
                        condition,
                        minimum,
                        maximum,
                        average,
                        sample_count,
                        recommendation,
                    )

                except ValueError:
                    # Ignore empty or incomplete startup data.
                    continue

    except serial.SerialException as error:
        print(f"Connection error: {error}")

    except KeyboardInterrupt:
        print("\nLighting Assistant stopped.")

        plot_session(readings)


if __name__ == "__main__":
    main()