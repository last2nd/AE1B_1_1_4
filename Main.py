import RPi.GPIO as GPIO
import time
import Elevator
import ServoRazorMotor
import Dominoes
import Hotwheels
import Plane	
import Catapult

HammerServoPin = #PWM #type: PWM
HammerButtonPin = #any #type: ignore

ElevatorControlPins = #any #type: ignore
ElevatorEndstopPin = #any #type: ignore
ElevatorShockSensorPin = #any #type: ignore

DistanceEcho = #any #type: ignore
DistanceTrig = #any #type: ignore
CarSolenoid = #any #type: ignore

CatapultRelayPin = #any #type:ignore
CatapultMicPin = #any #type:ignore

DcMotorInA = #any #type:ignore
DcMotorInB = #any #type:ignore
LightBarrierPin = #any #type:ignore

PlaneRelay = #any #type: ignore

InitOnOut = [PlaneRelay, CatapultRelayPin]
Out = [HammerServoPin,ElevatorControlPins, DistanceEcho, CarSolenoid, DcMotorInA, DcMotorInB]
In = [HammerButtonPin, ElevatorEndstopPin, ElevatorShockSensorPin, DistanceTrig, CatapultMicPin, LightBarrierPin]

def clean(In,Out,Init):
    for pins in In:
        GPIO.setup(pins, GPIO.IN)
    for pins in Out:
        GPIO.setup(pins, GPIO.OUT)
        GPIO.output(pins, GPIO.LOW)
    for pins in Init: #might not work as intended, must test
        GPIO.setup(pins, GPIO.OUT, initial=1)


if input("start program? y/n\n") == "y":
    GPIO.setmode(GPIO.BCM)
    clean(In, Out, InitOnOut)
    print("Pins initialized")
    #Plane.init(PlaneRelay) #no longer needed if works correctly
    #Catapult.init(CatapultRelayPin)
    time.sleep(5)
    print("Starting in 5")
    time.sleep(5)
    print("Starting Program")
    ServoRazorMotor.main(HammerServoPin, HammerButtonPin)
    print("Button has been hit!")
    time.sleep(0.5)
    clean(In, Out, InitOnOut)
    print("Activating Elevator")
    Elevator.main(ElevatorControlPins,ElevatorEndstopPin, ElevatorShockSensorPin)
    print("Elevator Finished")
    time.sleep(0.5)
    clean(In, Out, InitOnOut)
    print("Hotwheels Released")
    Hotwheels.main(DistanceEcho,DistanceTrig,CarSolenoid)
    print("Hotwheels Finished")
    time.sleep(0.5)
    clean(In, Out, InitOnOut)
    print("Launching Ball")
    Catapult.main(CatapultRelayPin, CatapultMicPin)
    print("Ball landed")
    time.sleep(0.5)
    clean(In, Out, InitOnOut)
    print("Dominoes Starting")
    Dominoes.main(DcMotorInA,DcMotorInB)
    print("Dominoes Finished")
    time.sleep(0.5)
    clean(In, Out, InitOnOut)
    print("Launching Plane")
    Plane.main(PlaneRelay)
    print("Program Finished")
    GPIO.cleanup()
else:
    GPIO.cleanup()
    exit(1)
