"""
@file:      ahtx0.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Concrete class for temperature and humidity from the Adafruit AHTx0
            sensor.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

from sensor.sensor import Sensor
from adafruit_ahtx0 import AHTx0 as _AHTx0

class AHTx0(Sensor):
    def __init__(self, i2c_bus) -> None:
        super().__init__()
        self.instance = _AHTx0(i2c_bus)
        self.datapoints["fields"]["temperature"] = None
        self.datapoints["fields"]["humidity"] = None

    def sample_sensor(self) -> None:
        super().sample_sensor()
        temperature = self.instance.temperature
        humidity = self.instance.relative_humidity
        
        self.datapoints["fields"]["temperature"] = temperature
        self.datapoints["fields"]["humidity"] = humidity

        print(f"{self.datapoints['timestamp']}\tTemperature (C): {temperature:.3f}\tHumidity (%): {humidity:.3f}")
