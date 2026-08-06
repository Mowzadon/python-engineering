import time

import serial
from serial.tools import list_ports

from config import (
    ARDUINO_PORT_KEYWORDS,
    BAUD_RATE,
    SERIAL_TIMEOUT,
)


def find_arduino_port():
    """
    Searches the computer's serial ports for a likely Arduino connection.

    Returns:
        str | None:
            The Arduino port name if one is found, otherwise None.
    """
    available_ports = list_ports.comports()

    for port in available_ports:
        device_name = port.device.lower()

        if any(
            keyword in device_name
            for keyword in ARDUINO_PORT_KEYWORDS
        ):
            return port.device

    return None


def open_arduino_connection():
    """
    Finds the Arduino and opens a serial connection.

    Returns:
        serial.Serial:
            An active serial connection to the Arduino.

    Raises:
        serial.SerialException:
            If no Arduino is found or the connection cannot be opened.
    """
    port = find_arduino_port()

    if port is None:
        raise serial.SerialException(
            "No Arduino serial port was found."
        )

    connection = serial.Serial(
        port,
        BAUD_RATE,
        timeout=SERIAL_TIMEOUT,
    )

    # Opening a connection normally resets an Arduino Uno.
    time.sleep(2)

    return connection


def read_light_data(connection):
    """
    Reads and parses one valid light measurement from the Arduino.

    Args:
        connection (serial.Serial):
            Active Arduino serial connection.

    Returns:
        tuple:
            A tuple containing:
                - light_level (int)
                - condition (str)

    Raises:
        ValueError:
            If the received line has an invalid format.
    """
    raw_line = connection.readline()

    if not raw_line:
        raise ValueError("No serial data received.")

    line = raw_line.decode("utf-8").strip()

    light_text, condition = line.split(",", maxsplit=1)
    light_level = int(light_text)

    if not 0 <= light_level <= 1023:
        raise ValueError(
            f"Light reading is outside the valid range: {light_level}"
        )

    return light_level, condition