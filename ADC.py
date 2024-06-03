import RPi.GPIO
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus (I2C must be ENABLED on the Pi!!)
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
"""'
channels = []
# Create single-ended input on channel 0
channels.append(AnalogIn(ads, ADS.P0))

print(f"{'raw':>5}\t{'v':>5}")
start_time = time.time()
while time.time() - start_time < 10:
    for idx, channel in enumerate(channels):
        print(f"channel {idx}: {channel.value}, {channel.voltage:.3f}\t", end="")
    print(end="\n")
    time.sleep(0.025)
"""


# returns supplied channel data in an array format
def ADCRead(pin):
    channel = AnalogIn(ads, ADS.Channel)
    return [channel.value, channel.voltage]
