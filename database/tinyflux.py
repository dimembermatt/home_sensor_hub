"""
@file:      couchdb.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Concrete class for implementing a couchdb backend.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

from database.database import Database
from tinyflux import TinyFlux, Point

class TinyfluxDB(Database):
    def __init__(self, file_path='./data/db.csv') -> None:
        super().__init__()
        self.db = TinyFlux(file_path)
    
    def add_datapoint(self, timestamp, tags, fields) -> None:
        p = Point(
            time=timestamp,
            tags=tags,
            fields=fields 
        )
        self.db.insert(p, compact_key_prefixes=True)


    # def add_series(self, series_name: str, series_type) -> None:
    #     pass
    
    # def remove_series(self, series_name: str, series_type) -> None:
    #     pass

    # def get_series(self, series_name: str):
    #     pass
