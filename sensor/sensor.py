"""
@file:      sensor.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Abstract class that provides the relevant interface for various sensors.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

from abc import ABC, abstractmethod
from datetime import datetime, timezone

class Sensor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.datapoints = {
            "timestamp": None,
            "tags": {},
            "fields": {}
        }

    @abstractmethod
    def sample_sensor(self) -> None:
        self.datapoints["timestamp"] = datetime.now(timezone.utc)

    def get_datapoint(self):
        return self.datapoints.values()
