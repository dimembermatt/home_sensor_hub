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
import time
from sensor.sgp30 import SGP30
from sensor.apds9960 import APDS9960
from sensor.ahtx0 import AHTx0
from database.tinyflux import TinyfluxDB

class Home_Sensor_Hub:
    def __init__(self) -> None:
        # Initialize the I2C connection.
        i2c = board.I2C()
        
        self.sensors = {}
        with open("config.json", "r") as fp:
            config = json.load(fp)

            # Initialize the database.
            database_impl = config["database"]["implementation"]
            self.db = None
            match database_impl:
                case "couchdb":
                    self.db = TinyfluxDB()
                case _:
                    pass
            print(self.db)
            
            # Initialize the webserver.

            # Initialize the sensors.
            for sensor_name, sensor_config in config["sensors"].items():
                sample_freq = sensor_config["sample_rate_hz"]
                sensor_instance = None
                sensor_thread = None
                
                match sensor_name:
                    case "SGP30":
                        sensor_instance = SGP30(i2c)
                        # TODO: start timer thread for each sensor to sample at given frequency
                        sensor_thread = threading.Thread(target=self.sensor_sample, args=["SGP30", sample_freq])
                    case "APDS9960":
                        sensor_instance = APDS9960(i2c)
                        sensor_thread = threading.Thread(target=self.sensor_sample, args=["APDS9960", sample_freq])
                    case "AHTx0":
                        sensor_instance = AHTx0(i2c)
                        sensor_thread = threading.Thread(target=self.sensor_sample, args=["AHTx0", sample_freq])
                    case _:
                        pass
                    
                self.sensors[sensor_name] = {
                    "instance": sensor_instance,
                    "thread": sensor_thread
                }
                
                sensor_thread.start()

    def sensor_sample(self, sensor_name, sample_freq):
        print(sensor_name, sample_freq)
        while True:
            self.sensors[sensor_name]["instance"].sample_sensor()
            timestamp, tags, fields = self.sensors[sensor_name]["instance"].get_datapoint()
            # Insert datapoint into db
            self.db.add_datapoint(timestamp, tags, fields)
                
            time.sleep(1.0 / sample_freq)

    def quit(self):
        # TODO: this
        pass