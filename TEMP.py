import Adafruit_DHT
import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

while True:
    humidity,temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,2)
    print(humidity,temperature)

GPIO.cleanup()