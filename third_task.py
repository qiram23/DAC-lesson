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

GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(50) 

try:

    while True:
        dutycycle=input("Введите число в процентах(q to exit): ")
        if dutycycle.isdigit():
            p.ChangeDutyCycle(int(dutycycle))
        elif dutycycle=='q':
            break
            p.stop()
        else:
            continue


finally:
    GPIO.output(22,GPIO.LOW)
    GPIO.cleanup(22)
    print("GPIO cleanup completed")