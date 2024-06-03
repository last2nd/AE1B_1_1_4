import RPi.GPIO as GPIO
import time


def activate_dc_motor(ina, inb):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ina, GPIO.OUT)
    GPIO.setup(inb, GPIO.OUT)
    GPIO.output(ina, GPIO.HIGH)
    GPIO.output(inb, GPIO.LOW)
    print("DC Motor Activated")
    time.sleep(10)
    print("DC Motor deActivated")
    time.sleep(1)
    GPIO.output(inb, GPIO.HIGH)
    GPIO.output(ina, GPIO.LOW)
    print("DC Motor Activated")
    time.sleep(10)
    print("DC Motor deActivated")
    GPIO.output(ina, GPIO.LOW)
    GPIO.output(inb, GPIO.LOW)
    GPIO.cleanup()
    # change to implement motor stop on sensor activation!!


def main(ina, inb):
    activate_dc_motor(ina, inb)
