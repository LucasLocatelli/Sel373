import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM) #extrai a pinagem da placa que esta sendo usada
GPIO.setwarnings(False)
saidas = (0, 4, 17, 22, 10, 11, 14, 15)
entradas = (23, 24)
GPIO.setup(saidas, GPIO.OUT)
GPIO.setup(entradas, GPIO.IN)

from firebase import firebase #importa a biblioteca de compatibilidade com firebase

firebase = firebase.FirebaseApplication('https://autohome-cfe1f.firebaseio.com/', None) 

GPIO.output(saidas, False)

#bounce time is given in ms and represents the mininum time between two callbacks
GPIO.add_event_detect(23, GPIO.RISING, bouncetime=5000)
def my_callback_rising(self):
    luz = firebase.get('/users/2www/Luz', None)
    print("rising")
    if luz is not None:
        chave=list(luz.keys())[0]
        firebase.delete('/Luz', chave)
        firebase.post('/users/2www/Log', {'teste':'acesa manualmente'})#str(Datetime.now())
        firebase.post('/Luz', {'status':'acesa'})
    else:
        firebase.post('/Log', {'teste' : 'acesa manualmente'})
        firebase.post('/Luz', {'status':'acesa'})
GPIO.add_event_callback(23, my_callback_rising)
GPIO.add_event_detect(24, GPIO.FALLING, bouncetime=5000)
def my_callback_falling(self):
    luz = firebase.get('/users/2www/Luz', None)
    print("falling")
    if luz is not None:
        chave=list(luz.keys())[0]
        firebase.delete('/Luz', chave)
        firebase.post('/users/2www',None, {'teste':'apagada manualmente'})
        firebase.post('/Luz', {'status':'apagada'})
    else:
        firebase.post('/Log', {'teste':'apagada manualmente'})
        firebase.post('/Luz', {'status':'apagada'})
GPIO.add_event_callback(24, my_callback_falling)

while True:
    result = firebase.get('/TipoCafe', None)
    luz = firebase.get('/status', None)
#status luz
#Luz
    if luz is not None:
        estado =list(luz.values())[0]
        if estado == "apagada":
            print("luz apagada")
            GPIO.output(15, False)
        elif estado == "acesa":
            print("luz acesa")
            GPIO.output(15, True)
#Cafeteira 	
    if result is not None:
        resultado = list(result.values())[0]
        chave = list(result.keys())[0]   
        #if resultado == "cafeteira_power_on": 
           # print("cafeteira ligada") 
           # GPIO.output(14, True)
        if resultado == "expresso" or resultado =="Expresso":
            print(resultado)
            GPIO.output(0,True)
            time.sleep(10)
            firebase.delete('/TipoCafe', chave)
            GPIO.output(0,False)
        elif resultado == "duplo" or resultado == "Duplo":
            print(resultado)
            GPIO.output(4, True)
            time.sleep(10)
            firebase.delete('/TipoCafe', chave)
            GPIO.output(4,False)
        elif resultado == "cappuccino" or resultado == "Cappuccino":
            print(resultado)
            GPIO.output(17, True)
            time.sleep(10)
            firebase.delete('/TipoCafe', chave)
            GPIO.output(17,False)
        elif resultado == "latte" or resultado == "Latte":
            print(resultado)
            GPIO.output(22, True)
            time.sleep(10)
            firebase.delete('/TipoCafe', chave)
            GPIO.output(22,False)
        elif resultado == "americano" or resultado == "Americano":
            print(resultado)
            GPIO.output(10, True)
            time.sleep(10)
            firebase.delete('/TipoCafe', chave)
            GPIO.output(10,False)
        elif resultado == "mooca" or resultado == "Mooca":
            print(resultado)
            GPIO.output(11, True)
            time.sleep(10)
            firebase.delete('/TipoCafe', chave)
            GPIO.output(11,False)
GPIO.cleanup()
