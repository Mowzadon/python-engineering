import pandas as pd
import matplotlib.pyplot as plt

#Main program loop
def main(): 

    #Create dataframe around temperature_data.csv
    data = pd.read_csv("temperature_data.csv")

    # Sensor Summary
    print("\nEngineering Sensor Report")
    print("-" * 40)
    print()

    print(f"Average Temperature: {data['Temperature'].mean():.2f} °C")
    print(f"Maximum Temperature: {data['Temperature'].max():.2f} °C")
    print(f"Minimum Temperature: {data['Temperature'].min():.2f} °C")
    print()

    print(f"Average Pressure: {data['Pressure'].mean():.2f} kPa")
    print(f"Maximum Pressure: {data['Pressure'].max():.2f} kPa")
    print(f"Minimum Pressure: {data['Pressure'].min():.2f} kPa")
    print()

    print(f"Average Humidity: {data['Humidity'].mean():.2f}%")
    print(f"Maximum Humidity: {data['Humidity'].max():.2f}%")
    print(f"Minimum Humidity: {data['Humidity'].min():.2f}%")
    print()

    print(f"Average Vibration: {data['Vibration'].mean():.2f}")
    print(f"Maximum Vibration: {data['Vibration'].max():.2f}")
    print(f"Minimum Vibration: {data['Vibration'].min():.2f}")

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

    fig, ax1 = plt.subplots(figsize=(10,5)) #create a figure 10" by 5"
    ax1.plot(
        data['Time'], 
        data['Temperature'], 
        marker="o",
        label="Temperature") #create line (x,y)

    ax1.set_title("Temperature Over TIme")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)")

    ax1.axhline(
        temperature_limit,
        linestyle = '--',
        label = 'Temperature Limit',
        color = 'orange'
    )

    ax1.legend()

    
    ax1.grid(True)

    
    plt.show()

if __name__ == "__main__":
    main()