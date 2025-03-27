# IoT Device Simulation & Data Analysis

## Overview
This project simulates an **IoT temperature sensor** that sends data to a Flask server using **token-based authentication**. The server validates incoming requests, stores the data, and provides **data visualization** using Matplotlib.

## Features
✅ Simulated **IoT temperature sensor** sending real-time data  
✅ **Token-based authentication** for secure data transfer  
✅ **Data storage in JSON format** for later analysis  
✅ **Graphical visualization** of temperature readings over time  
✅ **Zero Trust Security** principles applied (authentication & encryption)

---

## Project Structure
```
📂 IoT-Simulation-Project
│── iot-device.py      # Simulates IoT device (sends temperature data)
│── server.py          # Flask server (handles authentication & data storage)
│── analytics.py       # Reads and visualizes stored data
│── iot_data.json      # Stores received temperature readings
│── README.md          # Documentation
```

---

## 🔧 Setup & Installation

### 1️⃣ Install Required Dependencies
Ensure you have Python **3.8+** installed, then install required packages:

Create and activate virtual environment

```bash
    python3 -m venv venv
    source activate venv
```


```bash
pip install flask requests itsdangerous matplotlib
```

### 2️⃣ Start the Flask Server
Run the **server.py** to listen for incoming IoT data:
```bash
python server.py
```
This will start a Flask server at `http://127.0.0.1:5000/`

### 3️⃣ Get Authentication Token
Obtain an authentication token for secure communication:
```bash
curl http://127.0.0.1:5000/get-token
```
Copy the token and update `AUTH_TOKEN` in `iot-device.py`.

### 4️⃣ Start the IoT Device Simulation
Run the **IoT device script** to generate and send temperature readings:
```bash
python iot-device.py
```
This will continuously send simulated temperature data to the server.

### 5️⃣ Visualize Data
Run the **analytics script** to plot temperature readings over time:
```bash
python analytics.py
```
A graph will be displayed showing temperature variations.

---

## 🚀 How It Works

### **1. IoT Device Simulation (`iot-device.py`)**
- Generates a **random temperature** between 20°C - 35°C every **2 seconds**.
- Computes a **running average** of the last 5 readings.
- Sends the data to the server using **token-based authentication**.

### **2. Flask Server (`server.py`)**
- Provides an endpoint to **generate a token** (`/get-token`).
- Validates the **Bearer Token** before accepting data (`/iot-data`).
- Stores received temperature readings in **`iot_data.json`**.

### **3. Data Analysis (`analytics.py`)**
- Reads data from `iot_data.json`.
- Extracts **timestamps & temperature values**.
- Plots a **line graph** using Matplotlib.

---

## 🔐 Security Features
✔ **Token-based authentication**: Only authorized devices can send data.  
✔ **Bearer Token Validation**: Prevents unauthorized access.  
✔ **Data Encryption (HTTPS recommended)**: Secure transmission in real-world usage.  

---

## 📈 Example Output
After running `iot-device.py`, you should see:
```
Current Temperature: 25.4 °C | Running Average: 24.9 °C
Data sent successfully
Current Temperature: 26.8 °C | Running Average: 25.6 °C
Data sent successfully
...
```
Running `analytics.py` will generate a **graph** of temperature readings over time. 📊

---

## 🚀 Future Enhancements
- ✅ Store data in a **database** (e.g., SQLite, PostgreSQL)
- ✅ Implement **real-time data visualization** (using WebSockets)
- ✅ Enhance **security with Multi-Factor Authentication (MFA)**

---

## 🔗 License
This project is **open-source** and can be used for learning and development purposes. 🚀

