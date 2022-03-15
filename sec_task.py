import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3


def decimal2binary(decimal):
    return[int(bit) for bit in bin(decimal)[2:].zfill(bits)]


def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    time.sleep(0.01)
    return signal


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)

try:
    for i in range(levels):
        signal = bin2dac(i)
    for i in range(levels-1, -1, -1):
        signal=bin2dac(i)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")
