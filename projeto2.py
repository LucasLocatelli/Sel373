import time
from gpiozero import LEDBoard, Button

saidas = LEDBoard(0, 4, 17, 22, 10, 11, 14, 15)
entradas = Button(23)

from firebase import firebase #importa a biblioteca de compatibilidade com firebase

firebase = firebase.FirebaseApplication('https://autohome-cfe1f.firebaseio.com/', None) 

saidas.off()

#bounce time is given in ms and represents the mininum time between two callbacks
GPIO.add_event_detect(23, GPIO.RISING, bouncetime=5000)
def my_callback_luz(self):
    luz = firebase.get('/status_luz', None)
    if GPIO.input(23) == True:
        print("funciona")
        if luz is not None:
            chave=list(luz.keys())[0]
            firebase.delete('/status_luz', chave)
            firebase.post('/status', "acender")
            firebase.post('/status_luz', "acender")
        else:
            firebase.post('status', "acender")
            firebase.post('status_luz', "acender")
    elif GPIO.input(23) == False:
        print("funciona2")
        if luz is not None:
            chave=list(luz.keys())[0]
            firebase.delete('/status_luz', chave)
            firebase.post('/status', "apagar")
            firebase.post('/status_luz', "apagar")
        else:
 
while True:
    result = firebase.get('/TipoCafe', None)
    luz = firebase.get('/status_luz', None)
#status luz
#Luz
    if luz is not None:
        estado =list(luz.values())[0]
        if estado == "apagar":
            print("luz apagada")
            GPIO.output(15, False)
        elif estado == "acender":
            print("luz acessa")
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



  

