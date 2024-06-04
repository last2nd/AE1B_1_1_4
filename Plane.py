import RPi.GPIO as GPIO  # type: ignore
import time

GPIO.setmode(GPIO.BCM)


def main(Relay):
    GPIO.setup(Relay, GPIO.OUT)
    GPIO.output(Relay, GPIO.LOW)


def init(Relay):
    GPIO.setup(Relay, GPIO.OUT)
    GPIO.output(Relay, GPIO.HIGH)
