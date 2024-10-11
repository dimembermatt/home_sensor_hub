"""
@file:      apds9960.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Concrete class for measuring proximity, gestures, and ambient light
            from the Adafruit APDS9960 sensor.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

from sensor.sensor import Sensor
from adafruit_apds9960.apds9960 import APDS9960 as _APDS9960

class APDS9960(Sensor):
    def __init__(self, i2c_bus) -> None:
        super().__init__()
        self.instance = _APDS9960(i2c_bus)
        self.instance.enable_proximity = True
        self.instance.enable_gesture = True
        self.instance.enable_color = True
        # TODO: support for rotation
        # self.instance.rotation = 270
        self.datapoints["fields"]["proximity"] = None
        self.datapoints["fields"]["gesture"] = None
        self.datapoints["fields"]["color"] = None

    def sample_sensor(self) -> None:
        super().sample_sensor()

        proximity = self.instance.proximity
        # TODO: convert to enum class
        gesture = self.instance.gesture()
        color = None
        if self.instance.color_data_ready:
            r, g, b, c = self.instance.color_data
            color = [r, g, b, c]
            
        self.datapoints["fields"]["proximity"] = proximity
        self.datapoints["fields"]["gesture"] = gesture
        self.datapoints["fields"]["color"] = color

        print(f"{self.datapoints['timestamp']}\tProximity: {proximity}\tGesture: {gesture}\tColor: {color}")
