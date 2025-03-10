import firebase_admin
from firebase_admin import credentials, db
import RPi.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor  # Alternative DS18B20 library

# Load Firebase credentials (Replace with your actual Firebase key JSON file)
cred = credentials.Certificate("/home/pi/firebase-key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://live-measurements-a82ab-default-rtdb.firebaseio.com/"
})

# Initialize DS18B20 Sensor (Alternative method)
sensor = W1ThermSensor()

def read_temp():
    return round(sensor.get_temperature(), 2)  # Get temperature in Celsius

# TCS3200 Setup (Color Sensor)
S0 = 4
S1 = 17
S2 = 27
S3 = 22
OUT = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(OUT, GPIO.IN)

GPIO.output(S0, True)
GPIO.output(S1, False)

def read_color():
    GPIO.output(S2, False)
    GPIO.output(S3, False)
    red = measure_pulse()

    GPIO.output(S2, True)
    GPIO.output(S3, True)
    white = measure_pulse()

    return "white" if white < red else "red"

def measure_pulse():
    start = time.time()
    while GPIO.input(OUT) == GPIO.LOW:
        pass
    start = time.time()
    while GPIO.input(OUT) == GPIO.HIGH:
        pass
    end = time.time()
    return end - start

# Reference to Firebase database
ref = db.reference("measurements")

try:
    # Get DS18B20 temperature reading
    temperature = read_temp()

    # Get TCS3200 color reading
    color = read_color()

    # Create data entry
    data = {
        "temperature": temperature,
        "color": color,
        "timestamp": time.time()
    }

    # Send data to Firebase
    ref.set(data)
    print("Data Sent:", data)

except Exception as e:
    print("Error:", e)

finally:
    GPIO.cleanup()
    print("GPIO cleanup done!")
