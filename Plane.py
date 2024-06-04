import RPi.GPIO as GPIO  # type: ignore
import time

GPIO.setmode(GPIO.BCM)


def main(Relay):
    GPIO.setup(Relay, GPIO.OUT)
    GPIO.output(Relay, GPIO.LOW)


def init(Relay):  # shouldn't be needed but keeping just in case
    GPIO.setup(Relay, GPIO.OUT)
    GPIO.output(Relay, GPIO.HIGH)
