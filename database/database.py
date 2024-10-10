"""
@file:      database.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Abstract class that provides the relevant interface for various db backends.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""
from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    def add_series(self, series_name: str, series_type) -> None:
        pass
    
    def remove_series(self, series_name: str, series_type) -> None:
        pass
    
    @abstractmethod
    def add_datapoint(self, series_name: str, series_data) -> None:
        pass

    @abstractmethod
    def get_series(self, series_name: str):
