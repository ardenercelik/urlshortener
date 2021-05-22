from datetime import datetime
import string
from random import choices
import sys
from .extensions import db


# Integer, PRi key, URL, visitCount, date   CMD ["pipenv", "run", "flask", "run"]
class Link(db.Model):
    __tablename__ = "link"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)
    visit = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        charachers = string.digits + string.ascii_letters
        short_url = "".join(choices(charachers, k=5))

        link = self.query.filter_by(short_url=short_url).first()
        if link:
            return self.short-link()
        return short_url