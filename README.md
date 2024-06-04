# InHolland AE1B-1 Rube Goldberg Machine

This is the home for all the python code used on the Raspberry Pi for the Rube Goldberg Machine. All files expect Main.py are modules used in the machine. On operation the user only had to run Main.py.

# Code concept

Every file gets imported into main.py. This is where the user can specify the exact pins that they are using. All the initial setup happens here as well. Where a custom functions makes sure that after every action all pins are cleaned up to the exact amount we need them to be.
