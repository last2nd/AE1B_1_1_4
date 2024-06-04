import RPi.GPIO as GPIO
import time


def set_servo_angle(pwm, angle):
    # Duty cycle calculation for desired angle (adjust based on your servo)
    duty_cycle = (angle / 18) + 2.5
    pwm.ChangeDutyCycle(duty_cycle)


def move_servo(servo_pin, button_pin):
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(0)

    def button_callback():
        # Stop the program when button is pressed
        pwm.stop()
        exit()  # Exit the program

    # Add event detection for falling edge (button press) with debounce
    GPIO.add_event_detect(
        button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200
    )

    while True:
        for _ in range(20):  # Loop 20 times (underscore for unused variable)
            set_servo_angle(pwm, 0)  # Move to right
            time.sleep(0.2)
            set_servo_angle(pwm, 180)  # Move to left
            time.sleep(0.2)

        set_servo_angle(pwm, 90)  # Set to center position
        time.sleep(0.5)


# Main function now exits on button press
def main(servo_pin, button_pin):
    move_servo(servo_pin, button_pin)


if __name__ == "__main__":
    main()
