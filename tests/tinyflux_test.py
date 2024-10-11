from datetime import datetime, timezone
from tinyflux import TinyFlux, Point, FieldQuery, TagQuery, TimeQuery

db = TinyFlux('./data/db.csv') 

p = Point(
    time=datetime(2022, 5, 1, 16, 0, tzinfo=timezone.utc),
    tags={"room": "bedroom"},
    fields={"temp": 72.0}
)

db.insert(p, compact_key_prefixes=True)