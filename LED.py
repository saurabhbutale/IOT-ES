import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

While True:
      GPIO.output(3,True)
      time.sleep(0.5)
      GPIO.output(3,False)
      time.sleep(0.5)
      GPIO.output(13,True)
      time.sleep(0.5)
      GPIO.output(3,False)
      time.sleep(0.5)
GPIO.cleanup()


