### STATS CALCULATION
# Temperature 24.6C, Humidity 59.5%, Illumination 225 lx
# A19DC01C23B6FDD880 in Binary is 1010 0001 1001 1101 1100 0000 0001....

# First 10 Bits are Temeprature = 1010 0001 10 = 646
# Temperature Range is -40 to 60 for 0 to 1000 so 646 = -40 + 646/10 = 24.6 C

# Next 8 bits are Humidity = 01 1101 11 = 119
# Humidity Range is 0 to 100 for 0 to 200 so 119 = 119/2 = 83.5 %

# Next 17 bits are Illumination = 000000000111001001 =
# Illumination Range is 0 to 100,000 for 0 to 100,000 so 225 = 225 lx (edited)

class SensorDataConverter:

    def __init__(self, device_id, sensor_data):
        scale = 16
        num_of_bits = 8
        input_data = bin(int(sensor_data, scale))[2:].zfill(num_of_bits)

        self.temp_input = input_data[0:10]
        self.hum_input = input_data[10:18]
        self.illum_input = input_data[18:35]

        self.device_id = device_id

    # Returns the temperature in C
    def temp_range(self):
        output = (int(self.temp_input, 2) / 10) - 40
        return round(output, 2)

    # Returns humidity in %
    def hum_range(self):
        output = int(self.hum_input, 2)/2
        return round(output, 2)

    #Returns a rounded decimal of lx
    def illum_range(self):
        return round(int(self.illum_input, 2), 2)

    # Checks device ID and returns the name and location
    def sensor_location(self):
        device_location = ''
        device_name = ''
        if self.device_id == 'EnO_0420F51E':
            device_location = 'Near Green Roof'
            device_name = 'Red 1'
        elif self.device_id == 'EnO_0420FDDA':
            device_location = 'Near Control Slab'
            device_name = 'Red 2'
        elif self.device_id == 'EnO_0420F51F':
            device_location = 'Enviroment Temp'
            device_name = 'Red 3'
        return device_location, device_name

# Returns battery charge if available, returns False otherwise
def battery_reading(incoming_data):
    battery_reading = incoming_data[33:49]
    if 'batteryPercent' in battery_reading:
        battery_percent = incoming_data[49:53]
        return battery_percent
    return False
