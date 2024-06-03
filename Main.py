import Elevator
import ServoRazorMotor

HammerServoPin = #any
HammerButtonPin = #any

ElevatorControlPins = #any
ElevatorEndstopPin = #any

JoyInPin = #ADCChannel

if input("start program? y/n\n") == "y":
    print("Starting Program")
    ServoRazorMotor.main(HammerServoPin, HammerButtonPin)
    print("Activating Elevator")
    Elevator.ElevatorActivate(ElevatorControlPins,ElevatorEndstopPin)
    print("Elevator Finished")
else:
    exit(1)
