from i2c_scanner import I2CScanner
from Lib_oled import OLED
from machine import I2C
##******To scan your device bus I2C address write the pins to which you connect device according to the documentation******
bus=0
scl_Pin=1
sda_Pin=0
i2c=I2CScanner(bus, scl_Pin, sda_Pin)
##******Write addres of your device bus I2C address
screen_address=0x3c
screen=OLED(bus, scl_Pin, sda_Pin, screen_address)



screen.oled_on()
