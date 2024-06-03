import RPi.GPIO as GPIO
import time

motor_step_counter = 0

# Pin for endstop
# ButtonPin = 26

# Pins for stepper motor (from a-d)
# ControlPins = [25,8,7,1]

# Delay between steps, affects speed
step_sleep = 0.002

step_count = 4096  # 5.625*(1/64) per step, 4096 steps is 360°

direction = False  # True for clockwise, False for counter-clockwise

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]


def ElevatorActivate(ControlPins, ButtonPin):
    # setting up
    GPIO.setmode(GPIO.BCM)

    for pin in ControlPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    GPIO.setup(ButtonPin, GPIO.IN)

    def rotate_steps(steps, clockwise=True):
        global motor_step_counter
        direction = clockwise
        try:
            for _ in range(steps):
                for pin in range(0, len(ControlPins)):
                    GPIO.output(
                        ControlPins[pin], step_sequence[motor_step_counter][pin]
                    )
                if direction == True:
                    motor_step_counter = (motor_step_counter - 1) % 8
                else:
                    motor_step_counter = (motor_step_counter + 1) % 8
                time.sleep(step_sleep)
        except KeyboardInterrupt:
            cleanup()
            exit(1)

    def rotate_rotations(rotations, clockwise=True):
        steps_per_rotation = step_count
        total_steps = int(rotations * steps_per_rotation)
        rotate_steps(total_steps, clockwise)

    def cleanup():
        for pin in ControlPins:
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()

    try:
        while GPIO.input(ButtonPin) > 0:
            rotate_steps(1)
    except KeyboardInterrupt:
        cleanup()
        exit(1)
    finally:
        print("Endstop Reached")
        cleanup()


if __name__ == "__main__":
    ElevatorActivate()
