"""
@file:      couchdb.py
@author:    Matthew Yu (matthewjkyu@gmail.com)
@brief:     Concrete class for implementing a couchdb backend.
@version:   0.0.0
@date:      2024-10-03
@copyright: Copyright (c) 2024.
"""

import Database
from couchdb import Server
couch = couchdb.Server()

class CouchDB(Database):
    def __init__(self) -> None:
        super().__init__()
        self._server = Server()
        self._db = self._server.create('home_sensor_hub')
    
    def add_series(self, series_name, series_type) -> None:
        return super().add_series(series_name, series_type)
        