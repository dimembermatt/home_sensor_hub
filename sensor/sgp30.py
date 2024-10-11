"""
@file:      sgp30.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Concrete class for measuring equivalent CO2 and total volatile
            organic compounds from the Adafruit SGP30 sensor. 
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

from sensor.sensor import Sensor
from adafruit_sgp30 import Adafruit_SGP30

class SGP30(Sensor):
    def __init__(self, i2c_bus) -> None:
        super().__init__()
        self.instance = Adafruit_SGP30(i2c_bus)
        self.datapoints["fields"]["eCO2"] = None
        self.datapoints["fields"]["TVOC"] = None

        
    def sample_sensor(self) -> None:
        super().sample_sensor()

        eco2, tvoc = self.instance.iaq_measure()
        self.datapoints["fields"]["eCO2"] = eco2
        self.datapoints["fields"]["TVOC"] = tvoc

        print(f"{self.datapoints['timestamp']}\teCO2: {eco2:.3f}\tTVOC: {tvoc:.3f}")
