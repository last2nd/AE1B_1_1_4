import RPi.GPIO as GPIO
from time import sleep

# Relay_pin = None  # Relay module pin
# Micro_pin = None  # Microphone pin


# Something_happens = None  # Something suppose to happen before the weight will be dropped
# Something_happens_next = None
def init(Relay_pin):  # shouldn't be needed but keeping just in case
    GPIO.setup(Relay_pin, GPIO.OUT, initial=1)
    GPIO.output(Relay_pin, 1)


def main(Relay_pin, Micro_pin):
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


# GPIO.cleanup()
