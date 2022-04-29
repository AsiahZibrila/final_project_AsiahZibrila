from app import db
from sqlalchemy.dialects.postgresql import JSON


class Person(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text(), nullable=False, unique=True)
    #email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    reviews = db.relationship('Trip', backref='trip_driver', lazy=True)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Truck(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    id_num = db.Column(db.Text(), unique=True)
    #year = db.Column(db.Integer())
    reviews = db.relationship('Trip', backref='truck_trip', lazy=True)

    def __repr__(self):
        return '<Truck: {}>'.format(self.id_num)


class Trip(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    origin = db.Column(db.Text())
    destination = db.Column(db.Text())
    departure_date = db.Column(db.Text())
    route = db.Column(db.Text())
    comment = db.Column(db.Text())
    #rating = db.Column(db.Integer)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'))

    def __repr__(self):
        return '<Trip {}>'.format(self.route)


