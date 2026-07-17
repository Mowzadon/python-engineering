import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("temperature_data.csv")

print("========== Machine Temperature Report ==========\n")

print(f"Total Readings: {len(data.index)} ")

print(f"Average Temperature: {data["Temperature"].mean():.2f}") #prints avg temp rounded to 2 decimal places
print(f"Highest Temperature: {data["Temperature"].max():.2f}")
print(f"Lowest Temperature: {data["Temperature"].min():.2f}")

high_temperatures = data[data["Temperature"] > 22.5]
num_high_temps = len(high_temperatures)

print(f"\nHigh Temperature Readings (>22.5°C): {num_high_temps}\n")
print(high_temperatures)


hottest_row = data[data["Temperature"] == data["Temperature"].max()]
coldest_row = data[data["Temperature"] == data["Temperature"].min()]
print()
print(f"Row where highest temperature occurs:\n {hottest_row}")
print(f"\nRow where lowest temperature occurs:\n {coldest_row}")

abnormal_readings = data[(data["Temperature"] < 22.0) | (data["Temperature"] >  23.0)] #pandas uses & and | for 'and' and 'or' comparasons, each condition needs to be surrounded by a pair of ()
print(f"\nTemerature readings outside the range of 22.0°C and 23.0°C:\n {abnormal_readings}")

#matplot
#plt.figure(figsize=(8, 4)) #8" by 4"

#plt.plot(data["Time"], data["Temperature"], label = "Temperature", marker = "o") #draws a single line
#plt.plot(data["Time"], data["Pressure"], label = 'Pressure', marker = "x")

#plt.title("Machine Temperature Over Time")
#plt.xlabel("Time")
#plt.ylabel("Temperature (°C)")

#plt.grid(True)
#plt.legend()

#plt.show()

fig, ax1 = plt.subplots(figsize=(8, 4))

ax1.plot(
    data["Time"],
    data["Temperature"],
    marker="o",
    label="Temperature"
)

ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title("Machine Temperature and Pressure")
ax1.grid(True)

ax2 = ax1.twinx()

ax2.plot(
    data["Time"],
    data["Pressure"],
    marker="*",
    label="Pressure"
)

ax2.set_ylabel("Pressure (kPa)")

plt.show()