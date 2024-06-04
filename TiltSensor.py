import RPi.GPIO as GPIO
import time
import os
import csv

csvfile = "tilt_sensor_out.csv"
measure = False
sens_arr = []
time_arr = []


def main(tilt_sensor_pin):
    global measure
    measure = True
    while measure == True:
        sens_arr.append(GPIO.input(tilt_sensor_pin))
        time_arr.append(time.time())
        time.sleep(0.01)


def end():
    global measure
    measure = False
    with open(csvfile, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Time", "Value"])

        # Write the data rows
        for time, value in zip(time_arr, sens_arr):
            writer.writerow([time, value])
