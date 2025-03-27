import matplotlib.pyplot as plt
import json
import datetime

DATA_FILE = "iot_data.json"  # JSON file storing IoT data

# Load temperature data from file
try:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("Error: Could not read data file.")
    data = []

# Extract timestamps and temperatures
timestamps = []
temperatures = []

for entry in data:
    try:
        # Parse timestamp (assuming it's in ISO format)
        timestamp = datetime.datetime.fromisoformat(entry["time"])
        temperature = entry["temperature"]

        timestamps.append(timestamp)
        temperatures.append(temperature)
    except (KeyError, ValueError):
        print("Skipping invalid entry:", entry)

# Ensure there's data to plot
if not timestamps or not temperatures:
    print("No valid data to plot.")
else:
    # Plot temperature readings over time
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='b', label="Temperature (°C)")

    # Formatting the graph
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("IoT Device Temperature Readings Over Time")
    plt.legend()
    plt.xticks(rotation=45)  # Rotate timestamps for better visibility
    plt.grid(True)

    # Show the graph
    plt.show()
