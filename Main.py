import Elevator
import ServoRazorMotor

HammerServoPin = #any
HammerButtonPin = #any

ElevatorControlPins = #any
ElevatorEndstopPin = #any
ElevatorShockSensorPin = #any

JoyInPin = #ADCChannel

if input("start program? y/n\n") == "y":
    print("Starting Program")
    ServoRazorMotor.main(HammerServoPin, HammerButtonPin)
    print("Button has been hit!")
    print("Activating Elevator")
    Elevator.main(ElevatorControlPins,ElevatorEndstopPin, ElevatorShockSensorPin)
    print("Elevator Finished")
else:
    exit(1)
