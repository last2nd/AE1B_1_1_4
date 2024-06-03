import Elevator
import ServoRazorMotor

HammerServoPin = #any #type: ignore
HammerButtonPin = #any #type: ignore

ElevatorControlPins = #any #type: ignore
ElevatorEndstopPin = #any #type: ignore
ElevatorShockSensorPin = #any #type: ignore

JoyInPin = #ADCChannel #type: ignore

if input("start program? y/n\n") == "y":
    print("Starting Program")
    ServoRazorMotor.main(HammerServoPin, HammerButtonPin)
    print("Button has been hit!")
    print("Activating Elevator")
    Elevator.main(ElevatorControlPins,ElevatorEndstopPin, ElevatorShockSensorPin)
    print("Elevator Finished")
else:
    exit(1)
