"""
@file:      home_sensor_hub.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Top level class that manages the home sensor hub.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

import board
import json
import threading
from sensor.sgp30 import SGP30
from sensor.apds9960 import APDS9960
from sensor.ahtx0 import AHTx0
from database.couchdb import CouchDB

class Home_Sensor_Hub:
    def __init__(self) -> None:
        # Initialize the I2C connection.
        i2c = board.I2C()
        
        self.sensors = {}
        with open("config.json", "r") as fp:
            config = json.load(fp)

            # Initialize the sensors.
            for sensor_name, sensor_config in config["sensors"].items():
                sample_freq = sensor_config["sample_rate_hz"]
                signals = sensor_config["signals"]
                sensor_instance = None
                match sensor_name:
                    case "SGP30":
                        sensor_instance = SGP30(i2c)
                        # TODO: start timer thread for each sensor to sample at given frequency
                        threading.Thread()
                    case "APDS99960":
                        sensor_instance = APDS9960(i2c)
                    case "AHTx0":
                        sensor_instance = AHTx0(i2c)
                    case _:
                        pass
                self.sensors[sensor_name] = {
                    "instance": sensor_instance,
                    "signals": signals,
                }

            # Initialize the database.
            database_impl = config["database"]["implementation"]
            self.db = None
            match database_impl:
                case "couchdb":
                    self.db = CouchDB()
                case _:
                    pass
        
            # Initialize the webserver.

    def sensor_sample(self, sensor_name):
        self.sensors[sensor_name]["instance"].sample_sensor()
        for signal_name in self.sensors[sensor_name]["signals"].keys():
            datapoint = self.sensors[sensor_name]["instance"].get_datapoint(signal_name)
            # Insert datapoint into db
            self.db.insert(signal_name, datapoint)

    def quit(self):
        # TODO: this
        pass