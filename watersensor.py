import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(13,GPIO.OUT)

while True:
    var=GPIO.input(3)
    print(var)
    if var==1;
        GPIO.output(13,True)
    else:
        GPIO.output(13.False)
GPIO.cleanup()        