## Scanner for device i2c bus address
## Connect your RPI Pico and screen to the SDA and SCL. Remember write correct ID of i2c (0 or 1).
## I used ID of i2c=0 and scl=GPIO1, sda=GPIO0

from machine import Pin, I2C

def I2CScanner(bus, scl_Pin, sda_Pin):

    try:
        i2c=I2C(bus, scl=Pin(scl_Pin), sda=Pin(sda_Pin))
        devices_list=i2c.scan()
        if devices_list:
           print(f"{len(devices_list)} devices found:")
           for device_number, device_address in enumerate(devices_list,start=1):
            print(f"{device_number} device found on address (HEX): {hex(device_address)}")
        else:
            print("No devices found on I2C bus")
            
    except Exception as error:
        print(f"An error occurred: {error}")


## call this function in the main file or here below
#bus=0
#scl_Pin=1
#sda_Pin=0
#i2c=I2CScanner(bus, scl_Pin, sda_Pin)
