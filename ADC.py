import RPi.GPIO  # type: ignore
import time, board, busio  # type: ignore
import adafruit_ads1x15.ads1115 as ADS  # type: ignore
from adafruit_ads1x15.analog_in import AnalogIn  # type: ignore

# Create the I2C bus (I2C must be ENABLED on the Pi!!)
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)


# returns supplied channel data in an array format
def ADCRead(pin):  # pin should be in the following format: ADS.P0, ADS.P1,......
    channel = AnalogIn(ads, pin)
    return [channel.value, channel.voltage]
