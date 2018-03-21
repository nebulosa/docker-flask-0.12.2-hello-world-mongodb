from datetime import datetime

from . import db

class Request(db.Document):
    log       = db.StringField(required=True)
    datestamp = db.DateTimeField(default=datetime.now)
