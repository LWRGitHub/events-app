"""Database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

# Model called `Guest` with the following fields:
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False)

    # - events_attending: relationship to "Event" table with a secondary table
    events_attending = db.relationship('Event', secondary='guest_event_table', back_populates='guests')

    def __str__(self):
        return f'<Guest: {self.name}>'

    def __repr__(self):
        return f'<Guest: {self.name}>'

# `event_type` as an Enum column that denotes the
# type of event 
class Event_type(enum.Enum):
    PARTY = 1
    STUDY = 2
    NETWORKING = 3
    ALL = 4

# model called `Event` with the following fields:
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date_and_time = db.Column(db.Integer, nullable=False)
    guests = db.relationship('Guest', secondary='guest_event_table', back_populates='events_attending')

    # `event_type` as an Enum column that denotes the
    # type of event 
    event_type = db.Column(db.Enum(Event_type), default=Event_type.ALL)

    def __str__(self):
        return f'<Event: {self.title}>'

    def __repr__(self):
        return f'<Event: {self.title}>'

# Table `guest_event_table` with the following columns:
guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'))
)