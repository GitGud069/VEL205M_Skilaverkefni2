import firebase_admin
from firebase_admin import credentials, db
import time
import random  # Simulating sensor data (Replace with actual sensor readings)

# Load Firebase credentials (Replace with your actual Firebase key JSON file)
cred = credentials.Certificate("/home/pi/firebase-key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://live-measurements-a82ab-default-rtdb.firebaseio.com/"
})

# Reference to the database node
ref = db.reference("measurements")

while True:
    # Simulated temperature sensor reading (Replace with actual sensor data)
    temperature = round(random.uniform(700, 1500), 2)  # Example: Temperature in °C

    # Determine color state based on temperature
    if temperature >= 1000:
        color = "white"
    else:
        color = "red"

    # Create data entry
    data = {
        "temperature": temperature,
        "color": color,
        "timestamp": time.time()
    }

    # Send data to Firebase
    ref.set(data)
    print("Data Sent:", data)

    time.sleep(5)  # Send data every 5 seconds
