import numpy as np

# Temperature readings from an industrial machine (°C)
temperatures = np.array([
    21.4,
    22.1,
    23.0,
    22.7,
    21.9,
    22.5,
    23.2,
    22.8,
    21.7,
    22.3
])

print("Temperature Readings")
print(temperatures)

print()

print(f"Average Temperature: {np.mean(temperatures):.2f} °C") #:.2f -prints to second decimal place
print(f"Highest Temperature: {np.max(temperatures):.2f} °C")
print(f"Lowest Temperature: {np.min(temperatures):.2f} °C")
print(f"Standard Deviation: {np.std(temperatures):.2f} °C")

print()

print("Temperatures above 22.5°C")
print(temperatures > 22.5)

print()

print("Actual temperatures above 22.5°C:")
print(temperatures[temperatures > 22.5])

high_temperatures = temperatures[temperatures > 22.5] 

print("\nHigh Temperature Report")
print(high_temperatures)

print(f"Number of high readings: {len(high_temperatures)}")
print(f"Average high temperature: {np.mean(high_temperatures):.2f} °C")