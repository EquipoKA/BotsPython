import RPi.GPIO as GPIO
import time
import camera

def pir_mode (bot, update, chat_id):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)
    GPIO.setup(27, GPIO.IN) #PIR
    intentos=0
    while True:
        if GPIO.input(27):
            print("Motion Detected...")
            # camera.authoCam(bot,update,chat_id)
            intentos = intentos + 1
            if (intentos > 50):
                print("Me cago en Dios en el puto sensor de los cojones, ostias putas ya, este insulto ocupa mas que el codigo del puto commit de los cojones")
                return
	    time.sleep(0.5) #Buzzer turns on for 0.5 sec
        else:
            print("Pero muevete por favor")
            intentos = intentos + 1
            print(intentos)
            if (intentos > 20):
                print("Hasta nunca hijo de la gran puta") # lo dejo
                return
