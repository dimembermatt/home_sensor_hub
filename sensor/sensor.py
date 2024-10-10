"""
@file:      sensor.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Abstract class that provides the relevant interface for various sensors.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

from abc import ABC, abstractmethod
import time

class Sensor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.datapoints = {}

    @abstractmethod
    def sample_sensor(self) -> None:
        self.sample_time = time.time()

    def get_datapoint(self, name: str):
        if name in self.datapoints:
            return self.datapoints[name]
        return [None, None]
