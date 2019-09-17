import RPi.GPIO as GPIO
import time
import os
import glob
import pyrebase
import sys


print(sys.path)


#conexion a firebase

config = {
    "apiKey": " ",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": "",
}



firebase = pyrebase.initialize_app(config)
db = firebase.database()


storage = firebase.storage()


#GPIO SETUP
GPIO.setmode(GPIO.BCM)
Button = 21
n = 1
GPIO.setup(Button,GPIO.IN)
#Loop
print("Program Running")
while 1 == 1:#ejecucion indefinida hasta que se precione ctrl+z 
  if GPIO.input(Button) == False:#cuendo el boton es presionado:
    print("Button Pressed")
    
    #    ------|    foto & timbre    |------ #
    #Se obtiene el archivo
    now = time.strftime("Date%m-%d-%yTime%H-%M-%S")
    #MComando dee sistema
      
    command = "bash oscmds.sh " +  str(now)
    
    # -- OSMC.sh is an Shell script that
    # -- is responsible for taking the picture and
    # -- Making the Doorbell Noise
    
    #run command
    os.system(command)
    #diagnostics
    jpg=".jpg"
    now2=now + jpg
    print("Filename:", now2)
    

    
    #metodo para subir imagen a firebse por medio de una variable pibote
    #para invocar el nombre con jpg de extension
    
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    storage = firebase.storage()
    myfile=now2
    cap= myfile
    storage.child("img/" + str(now2)).put(cap)
  
    
    print("Proceso terminado")
    #-space out for next "Press of Button"
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    print("La captura fue enviada con exito")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    
    
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
