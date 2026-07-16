import pandas as pd

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

print()
hottest_row = data[data["Temperature"] == data["Temperature"].max()]
print(f"Row where highest temperature occurs: {hottest_row}")





