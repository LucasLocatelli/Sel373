import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM) #extrai a pinagem da placa que esta sendo usada
GPIO.setwarnings(False)
saidas = (0, 4, 17, 22, 10, 11, 14, 15)
entradas = (23, 24)
GPIO.setup(saidas, GPIO.OUT)
GPIO.setup(entradas, GPIO.IN)

import pyrebase #importa a biblioteca de compatibilidade com firebase

config = {
    "apiKey" : "AlzaSyBQCtSX2w7qwRKvU2eYUbjikVzPROEc8XU",
    "authDomain" : "autohome-cfe1f.firebaseapp.com",
    "databaseURL" : "https://autohome-cfe1f.firebaseio.com",
    "storageBucket" : "autohome-cfe1f.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database() 

GPIO.output(saidas, False)

#bounce time is given in ms and represents the mininum time between two callbacks
GPIO.add_event_detect(23, GPIO.RISING, bouncetime=5000)
def my_callback_rising(self):
    luz = db.child("users").child("2www").child("Luz").get()
    print("rising")
    db.child("users").child("2www").child("Luz").child("status").set("acesa")
    db.child("users").child("2www").child("Log").child("teste").set("acesa manualmente")
GPIO.add_event_callback(23, my_callback_rising)
GPIO.add_event_detect(24, GPIO.FALLING, bouncetime=5000)
def my_callback_falling(self):
    luz = db.child("users").child("2www").child("Luz").get()
    print("falling")
    db.child("users").child("2www").child("Luz").child("status").set("apagada")
    db.child("users").child("2www").child("Log").child("teste").set("apagada manualmente")
GPIO.add_event_callback(24, my_callback_falling)

while True:
    luz = db.child("users").child("2www").child("Luz").get()
#status luz
#Luz
    if luz is not None:
        if luz.val()['status'] == "apagada":
            print("luz apagada")
            GPIO.output(15, False)
        elif luz.val()['status'] == "acesa":
            print("luz acesa")
            GPIO.output(15, True)
GPIO.cleanup()
