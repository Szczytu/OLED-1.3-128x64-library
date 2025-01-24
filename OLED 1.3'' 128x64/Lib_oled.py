from machine import Pin, I2C
class OLED:
    def __init__(self, bus, scl, sda, screen_address):
       self.i2c_bus=I2C(bus,scl=Pin(scl),sda=Pin(sda))
       self.screen_address=screen_address

    def send_control_byte(self, Co, DC):
        self.Co=Co
        self.DC=DC
        return bytes([Co << 7 | DC])
    
    def send_command(self, command):
        i2c_address=self.screen_address
        self.command=command
        control_byte=self.send_control_byte(0,0)
        self.i2c_bus.writeto(i2c_address, control_byte + bytes([command]))
    
    def oled_on(self):
        "Turn on OLED screen"
        self.send_command(0xAF)

    def oled_off(self):
        "Turn off OLED screen"
        self.send_command(0xAE)