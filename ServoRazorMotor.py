import RPi.GPIO as GPIO
import time

servo_pin = 26
button_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(0)

def button_callback():
    for i in range(20):  # Loop 15 times
        # Move servo arm to the right
        pwm.ChangeDutyCycle(2.5)
        time.sleep(0.2)

        # Move servo arm to the left
        pwm.ChangeDutyCycle(10.5)
        time.sleep(0.2)

    pwm.ChangeDutyCycle(7.5)
    time.sleep(0.5)

# Detect a falling edge on the button pin,(the state of the button pin changed from high to low) and debounce it with a 200ms delay



button_callback()
pwm.stop()
GPIO.cleanup()
