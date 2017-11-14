import RPi.GPIO as GPIO
import time
import camera



def pir_mode (bot, update, chat_id):
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(23, GPIO.IN) #PIR
   try:
      time.sleep(2) # to stabilize sensor
      while True:
          if GPIO.input(23):
	      time.sleep(0.5) #Buzzer turns on for 0.5 sec
              print("Motion Detected...")
              camera.authoVid(bot,update,chat_id)
	      time.sleep(5) #to avoid multiple detection
	      break
          time.sleep(0.1) #loop delay, should be less than detection delay
	  
   except:
      GPIO.cleanup()
