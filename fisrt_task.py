import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(decimal):
    return[int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT,initial = GPIO.LOW)

try:
    while True:
        inputStr=input("Enter a value between 0 and 255('q' to exit) > ")

        if inputStr.isdigit():
            value=int(inputStr)
            if value>=levels:
                print("The value is too large, try again")
                continue
            signal=bin2dac(value)
            voltage=value / levels * maxVoltage
            print("Entered value = {:^3} -> {}, output voltage = {:.2f}".format(value, signal, voltage))

        elif inputStr == 'q':
            break

        else:
            print("Enter a positive integer")
            continue        
finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")