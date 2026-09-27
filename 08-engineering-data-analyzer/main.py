import pandas as pd
import matplotlib.pyplot as plt


def print_sensor_summary(data, column, unit):
    """
    Prints the average, maximum, and minimum values
    for a specified sensor column in the DataFrame.

    Args:
        data (DataFrame): The sensor data.
        column (str): The name of the sensor column.
        unit (str): The unit to display (e.g., °C, kPa, %).

    """
    print(f"Average {column}: {data[column].mean():.2f} {unit}")
    print(f"Maximum {column}: {data[column].max():.2f} {unit}")
    print(f"Minimum {column}: {data[column].min():.2f} {unit}")
    print()

#Main program loop
def main(): 

    #Create dataframe around temperature_data.csv
    data = pd.read_csv("temperature_data.csv")

    # Sensor Summary
    print("\nEngineering Sensor Report")
    print("-" * 40)
    print()

    print_sensor_summary(data, "Temperature", "°C")
    print_sensor_summary(data, "Pressure", "kPa")
    print_sensor_summary(data, "Humidity", "%")
    print_sensor_summary(data, "Vibration", "")

    # Detecting abnormal readings
    temperature_limit = 24.0
    vibration_limit = 0.25

    high_temperature_readings = data[data['Temperature'] > temperature_limit]
    high_vibration_readings = data[data['Vibration'] > vibration_limit]

    print("\nAbnormal Temperature Readings")
    print("-" * 40)
    print(high_temperature_readings)

    print("\nAbnormal Vibration Readings")
    print("-" * 40)
    print(high_vibration_readings)

    # Abnormal reading alerts
    print("\nHigh Temperature Alert")
    print("-" * 40)

    for index, row in high_temperature_readings.iterrows():  # gives index and row together
        print(f"Time: {row['Time']}")
        print(f"Temperature: {row['Temperature']} °C")

    #Sensor graph
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,8)) #create a figure 10" by 8"

    #temperature graph
    ax1.plot(  #.plot() creates line (x,y)
        data['Time'], 
        data['Temperature'], 
        marker="o",
        label="Temperature")

    #horizontal line
    ax1.axhline(
        temperature_limit,
        linestyle = '--',
        label = 'Temperature Limit',
        color = 'orange'
    )

    ax1.plot(
    high_temperature_readings['Time'],
    high_temperature_readings['Temperature'],
    marker='o',
    linestyle='', #no line to be drawn
    markersize=10, #draws markers
    color='red',
    label='High Temperature'
)
    ax1.legend()
    ax1.grid(True)

    ax1.set_title("Temperature Over Time")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)")

    #vibration graph
    ax2.plot(
        data["Time"],
        data["Vibration"],
        marker = "o",
        label = "Vibration"
    )

    ax2.axhline( #.axhline() creates horizontal line
        vibration_limit,
        color="orange",
        linestyle="--",
        label = "Vibration Limit"
    )

    ax2.plot(
        high_vibration_readings["Time"],
        high_vibration_readings["Vibration"],
        marker="o",
        linestyle="",
        markersize=10,
        color="red",
        label="High Vibration"

    )

    ax2.legend()
    ax2.grid(True)

    ax2.set_title("Vibration Over Time")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Vibration")


    plt.tight_layout() #prevents overlapping labels
    plt.savefig("engineering_dashboard.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()