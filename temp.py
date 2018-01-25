import RPi.GPIO as GPIO
import dht11
import time
import datetime
import os

API_KEY = 6cd59ec020b1c8d2a796a37f07ceceee

DEVICE_ID = 43cc827943078783f235589b881a433e
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=17)

from m2x.client import M2XClient

client = M2XClient(key=os.environ['API_KEY'])

device = client.device(os.environ['DEVICE_ID'])

stream = device.create_stream('temp')

while True:
    result = instance.read()
    if result.is_valid():
        stream.add_value(result.temperature)
        time.sleep(10)

