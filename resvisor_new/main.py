import RPi.GPIO as GPIO
import time
import os

os.system('python3 /home/pi/Desktop/opencvtest3.py &')#main camera screen
#os.system('python3 /home/pi/Desktop/opencvtest5.py &')#Recording code
#os.system('python3 /home/pi/Desktop/opencvtest6.py &')#Take picture code

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Run Recording code
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Run Picture code
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)#To turn on Thermal Camera
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)#To turn off Thermal Camera
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Take Screenshot of screen

while True:       
    input_state = GPIO.input(26)
    if input_state == False:
        os.system('pkill -f opencvtest3.py &')
        os.system('pkill -f opencvtest6.py &')
        print('Recording ON')
        os.system('python3 /home/pi/Desktop/record.py &')
        time.sleep(2)
        os.system('pkill -f record.py &')
        os.system ('python3 /home/pi/Desktop/opencvtest5.py &')
        time.sleep(0.2)
        
    input_state = GPIO.input(6)
    if input_state == False:
        os.system('pkill -f opencvtest5.py &')
        os.system('pkill -f opencvtest3.py &')
        print('Image ON')
        os.system ('python3 /home/pi/Desktop/opencvtest6.py &')
        time.sleep(0.2)
        
    input_state = GPIO.input(16)#Open thermal
    if input_state == False:
        print('Thermal ON')
        os.system ('python3 /home/pi/Desktop/CHCK.py &')
        time.sleep(4)
        os.system ('pkill -f CHCK.py &')
        os.system ('python3 /home/pi/Desktop/second.py &')
        time.sleep(0.2)
        
    input_state = GPIO.input(5)#Close thermal
    if input_state == False:
            print('Thermal OFF')
            os.system('pkill -f second.py &')
            time.sleep(0.2)
            
    input_state = GPIO.input(25)#Take Screenshot of screen XD
    if input_state == False:
            print('SCREENSHOT TAKEN XD')
            os.system('scrot /home/pi/Desktop/Screenshots/%Y%m%d%S.png')
            os.system('python3 /home/pi/Desktop/CHCK1.py &')
            time.sleep(2)
            os.system('pkill -f CHCK1.py &')
            time.sleep(0.2)
            
    GPIO.cleanup()
     