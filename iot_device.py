import random
import time
import requests
import datetime

SERVER_URL = 'http://127.0.0.1:5000/iot-data'
AUTH_TOKEN = 'Bearer eyJpb3RfZGV2aWNlIjoic2Vuc29yXzEifQ.Z-Wn4Q.cUQWz-uaD81b3APcCKjcLWd7G5I'
# Replace with the token from the

def send_data_to_server(data):
    headers = {'Authorization': AUTH_TOKEN}
    response = requests.post(SERVER_URL, headers=headers, json=data)
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print(f"Failed to send data: {response.status_code}")


def simulate_temperature():
    """Simulating a temperature sensor (values between 20 and 35 degrees Celsius)"""
    return round(random.uniform(20, 35), 2)


def calculate_running_average(data_list):
    return sum(data_list) / len(data_list)

while True:
    readings =[]     
    temperature = simulate_temperature()
    readings.append(temperature)

    if len(readings) > 5: readings.pop(0)
    running_avg = calculate_running_average(readings)

    print(f"Current Temperature: {temperature} °C | Running Average: {running_avg:.2f} °C")
    data = {"temperature": temperature, "running_avg": running_avg,  "time": str(datetime.datetime.now())}

    send_data_to_server(data)
    time.sleep(2) 
