import RPi.GPIO as GPIO  # type: ignore
import time


# Set up GPIO pin


# Function to measure distance
def distance(GPIO_ECHO, GPIO_TRIGGER):
    # Set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # Set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    # Save start time
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # Save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Time difference   start and arrival
    time_elapsed = stop_time - start_time

    # Multiply with the speed of sound (34300 cm/s) and divide by 2
    distance = (time_elapsed * 34300) / 2

    return distance


# Function to control the solenoid
def loop(solenoid_pin, GPIO_ECHO, GPIO_TRIGGER):
    try:
        while True:
            dist = distance(GPIO_ECHO, GPIO_TRIGGER)
            if (
                dist < 10
            ):  # Adjust this value to trigger the solenoid at a certain distance
                GPIO.output(solenoid_pin, GPIO.HIGH)  # Turn on the solenoid
                print("Solenoid turned on")
            else:
                GPIO.output(solenoid_pin, GPIO.LOW)  # Turn off the solenoid
                print("Solenoid turned off")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")


def main(GPIO_ECHO, GPIO_TRIGGER, solenoid_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.setup(solenoid_pin, GPIO.OUT)
    loop(solenoid_pin, GPIO_ECHO, GPIO_TRIGGER)


# Run the loop function
if __name__ == "__main__":
    print("test")
    # loop()
