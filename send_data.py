from gpiozero import DigitalInputDevice, DigitalOutputDevice
import time

# TCS3200 Pin Setup
S0 = DigitalOutputDevice(4)
S1 = DigitalOutputDevice(17)
S2 = DigitalOutputDevice(27)
S3 = DigitalOutputDevice(22)
OUT = DigitalInputDevice(18)

S0.on()
S1.off()

def read_color():
    S2.off()
    S3.off()
    red = measure_pulse()

    S2.on()
    S3.on()
    white = measure_pulse()

    return "white" if white < red else "red"

def measure_pulse():
    start = time.time()
    while OUT.value == 0:  # Wait for LOW
        pass
    start = time.time()
    while OUT.value == 1:  # Wait for HIGH
        pass
    end = time.time()
    return end - start
