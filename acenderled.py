import RPi.GPIO as GPIO

LED1 = 26
LED2 = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

GPIO.output(LED1, False)
GPIO.output(LED2, False)
while True:
	GPIO.output(LED1, True)
	GPIO.output(LED2, True)
GPIO.cleanup()
