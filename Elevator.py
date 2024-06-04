import RPi.GPIO as GPIO  # type: ignore
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
    def rotate_steps(steps, clockwise=True):
        global motor_step_counter
        direction = clockwise
        try:
            for _ in range(steps):
                for pin in range(0, len(ControlPins)):
                    GPIO.output(
                        ControlPins[pin], step_sequence[motor_step_counter][pin]  # type: ignore
                    )
                if direction == True:
                    motor_step_counter = (motor_step_counter - 1) % 8
                else:
                    motor_step_counter = (motor_step_counter + 1) % 8
                time.sleep(step_sleep)
        except KeyboardInterrupt:
            exit(1)

    try:
        while GPIO.input(ButtonPin) > 0:
            rotate_steps(1)
    except KeyboardInterrupt:
        exit(1)
    finally:
        print("Endstop Reached")


def ShockDetect(ShockPin):
    while GPIO.input(ShockPin) < 1:
        time.sleep(0.1)


def main(ControlPins, ButtonPin, ShockPin):
    ElevatorActivate(ControlPins, ButtonPin)
    print("Endstop Reached")
    time.sleep(0.1)
    ShockDetect(ShockPin)
    print("Shock Detected!")


if __name__ == "__main__":
    # main()
    print("no pins")
