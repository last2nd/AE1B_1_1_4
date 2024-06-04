import RPi.GPIO as GPIO
from time import sleep

# Relay_pin = None  # Relay module pin
# Micro_pin = None  # Microphone pin

GPIO.setmode(GPIO.BCM)


# Something_happens = None  # Something suppose to happen befor the weight will be dropped
# Something_happens_next = None
def init(Relay_pin):
    GPIO.setup(Relay_pin, GPIO.OUT, initial=1)
    GPIO.output(Relay_pin, 1)


def main(Relay_pin, Micro_pin):
    GPIO.setup(Relay_pin, GPIO.OUT, initial=1)
    GPIO.setup(Micro_pin, GPIO.IN, initial=0)
    GPIO.output(Relay_pin, 0)
    print("The weight is dropped")
    while True:  # Microphone is waiting for ball
        try:
            if GPIO.output(Micro_pin, 1):
                print("Sound detected")
                # Something_happens_next = True  # When drop sound of the ball is detected something happens next
                break
            else:
                print("Microphone is waiting")
        except KeyboardInterrupt:
            print("STOP")
            GPIO.cleanup()


# GPIO.cleanup()