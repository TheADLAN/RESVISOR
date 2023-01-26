import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_UP)


num = 0
prnt = 0
last = 0

while True:
    input_value = gpio.input(26)

    if (input_value == 1) and (input_value != last):
        last = 1
        prnt = 1
        num += 1
        time.sleep(0.05)
        continue

    if (input_value == 0) and (input_value != last):
        last = 0
        time.sleep(0.05)
        continue

    if (input_value == 0) and (input_value == last):
        if (prnt == 1):
            if (num == 10):
                num = 0

            if (num == 0):
                print("0")
            if (num == 1):
                print("1")                
            if (num == 2):
                print("2")
            if (num == 3):
                print("3")
            if (num == 4):
                print("4")                
            if (num == 5):
                print("5")                
            if (num == 6):
                print("6")                
            if (num == 7):
                print("7")                
            if (num == 8):
                print("8")                
            if (num == 9):
                print("9")                


            num = 0
            prnt = 0
            last = 0
        continue