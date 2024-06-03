import time
import Elevator
import ServoRazorMotor
import Dominoes

HammerServoPin = #any #type: ignore
HammerButtonPin = #any #type: ignore

ElevatorControlPins = #any #type: ignore
ElevatorEndstopPin = #any #type: ignore
ElevatorShockSensorPin = #any #type: ignore

JoyInPin = #ADCChannel #type: ignore

DcMotorInA = #any #type:ignore
DcMotorInB = #any #type:ignore


if input("start program? y/n\n") == "y":
    print("Starting Program")
    ServoRazorMotor.main(HammerServoPin, HammerButtonPin)
    print("Button has been hit!")
    time.sleep(0.5)
    print("Activating Elevator")
    Elevator.main(ElevatorControlPins,ElevatorEndstopPin, ElevatorShockSensorPin)
    print("Elevator Finished")
    time.sleep(0.5)
    print("Dominoes Starting")
    Dominoes.main(DcMotorInA,DcMotorInB)
    print("Dominoes Finished")
    time.sleep(0.5)
else:
    exit(1)
