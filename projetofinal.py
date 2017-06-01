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
GPIO.add_event_detect(24, GPIO.BOTH, bouncetime=2000)
def my_callback_rising(self):
    luz = db.child("Reg_Boards").child("2www").child("Device").child("Luz").get()
    if luz.val()['status'] == "apagada":
        print("rising")
        db.child("Reg_Boards").child("2www").child("Device").child("Luz").child("status").set("acesa")
        db.child("Reg_Boards").child("2www").child("Log").child("Log_luz").child("data").set( "acesa manualmente")
        luz = db.child("Reg_Boards").child("2www").child("Device").child("Luz").get()
    else:
        print("falling")
        db.child("Reg_Boards").child("2www").child("Device").child("Luz").child("status").set("apagada")
        db.child("Reg_Boards").child("2www").child("Log").child("Log_luz").child("data").set("apagada manualmente")
GPIO.add_event_callback(24, my_callback_rising)

while True:
    cafe = db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("queue").get()
    luz = db.child("Reg_Boards").child("2www").child("Device").child("Luz").get()
    cafe_on = db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("Power").get()
#status luz
#Luz
    if luz.val() is not None:  
        if luz.val()['status'] == "apagada":
            print("luz apagada")
            GPIO.output(15, False)
        elif luz.val()['status'] == "acesa":
            print("luz acesa")
            GPIO.output(15, True)
#Cafeteira 	
    if cafe.val() is not None:
        if cafe_on.val()['status'] == "on": 
           print("cafeteira ligada") 
           GPIO.output(14, True)
        else:
           print("Cafeteira Desligada")
           GPIO.output(14, False)
        if cafe.val()['type'] == "expresso" or cafe.val()['type'] == "Expresso":
            print(cafe.val()['type'])
            GPIO.output(0,True)
            time.sleep(10)
            db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("queue").child("type").remove()
            GPIO.output(0,False)
        elif cafe.val()['type'] == "duplo" or cafe.val()['type'] == "Duplo":
            print(cafe.val()['type'])
            GPIO.output(4, True)
            time.sleep(10)
            db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("queue").child("type").remove()
            GPIO.output(4,False)
        elif cafe.val()['type'] == "cappuccino" or cafe.val()['type'] == "Cappuccino":
            print(cafe.val()['type'])
            GPIO.output(17, True)
            time.sleep(10)
            db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("queue").child("type").remove()
            GPIO.output(17,False)
        elif cafe.val()['type'] == "latte" or cafe.val()['type'] == "Latte":
            print(cafe.val()['type'])
            GPIO.output(22, True)
            time.sleep(10)
            db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("queue").child("type").remove()
            GPIO.output(22,False)
        elif cafe.val()['type'] == "americano" or cafe.val()['type'] == "Americano":
            print(cafe.val()['type'])
            GPIO.output(10, True)
            time.sleep(10)
            db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("queue").child("type").remove()
            GPIO.output(10,False)
        elif cafe.val()['type'] == "mooca" or cafe.val()['type'] == "Mooca":
            print(cafe.val()['type'])
            GPIO.output(11, True)
            time.sleep(10)
            db.child("Reg_Boards").child("2www").child("Device").child("Cafeteira").child("queue").child("type").remove()
            GPIO.output(11,False)
GPIO.cleanup()
