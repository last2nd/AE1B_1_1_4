import RPi.GPIO as GPIO
import time


def setup(servo_pin, button_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
    pwm.start(0)  # Initial duty cycle

    return pwm


def button_callback(pwm, channel):
    print("Button pressed!")
    for i in range(15):  # Loop 15 times
        # Move servo arm to the right
        pwm.ChangeDutyCycle(2.5)
        time.sleep(0.05)

        # Move servo arm to the left
        pwm.ChangeDutyCycle(4.5)
        time.sleep(0.05)


def main(servo_pin, button_pin):
    pwm = setup(servo_pin, button_pin)

    GPIO.add_event_detect(
        button_pin,
        GPIO.FALLING,
        callback=lambda channel: button_callback(pwm, channel),
        bouncetime=200,
    )

    try:
        while True:
            time.sleep(0.1)
    finally:
        pwm.stop()
        GPIO.cleanup()
