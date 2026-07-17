import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("temperature_data.csv")


#Sensor Summary

print("\nEngineering Sensor Report")
print("-"*40)

print(f"Average Temperature: {data["Temperature"].mean():.2f} °C")
print(f"Maximum Temperature: {data["Temperature"].max():.2f} °C")
print(f"Minimum Temperature: {data["Temperature"].min():.2f} °C")
