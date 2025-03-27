import os
from flask import Flask, json, request, jsonify
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
DATA_FILE = "iot_data.json"

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)  


# Generate token for device authentication
def generate_auth_token(expiration=600):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps({'iot_device': 'sensor_1'})


@app.route('/get-token', methods=['GET'])
def get_token():
    token = generate_auth_token()
    return jsonify({"token": token})


# Route to authenticate IoT device
@app.route('/iot-data', methods=['POST'])
def iot_data():
    token = request.headers.get('Authorization')
    print(token)

    if not token:
        return jsonify({"error": "Token is missing"}), 401

    # Extract token (remove 'Bearer ' prefix)
    token_parts = token.split()
    if len(token_parts) != 2 or token_parts[0] != "Bearer":
        return jsonify({"error": "Invalid token format"}), 401

    token = token_parts[1]
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token, max_age=600)
        if data.get('iot_device') == 'sensor_1':
            received_data = request.get_json()
            print(received_data)

              # Save data to JSON file
            with open(DATA_FILE, "r+") as f:
                existing_data = json.load(f) 
                existing_data.append(received_data)
                f.seek(0)
                json.dump(existing_data, f, indent=4) 

            return jsonify({"status": "Data received", "data": received_data}), 200
    except Exception as e:
        return jsonify({"error": "Unauthorized access: "+ str(e)}), 401

if __name__ == '__main__':
    app.run(debug=True)
