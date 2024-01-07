from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from Search_pg.main.application import app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///client_database.db"
app.config["SQLALCHEMY_BINDS"] = {"second" : "sqlite:///user_database.db"}
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType


db = SQLAlchemy(app)


class Client(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    firstname = db.Column(db.String(999),nullable=False)
    lastname = db.Column(db.String(999),nullable=False)
    email = db.Column(db.String(999),unique=True)
    password = db.Column(db.String(999),nullable=False)
    created_by = db.Column(db.String(999))
    hostels = db.relationship('Hostel', backref='owner',lazy=True)


class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    hostel_name = db.Column(db.String(999),nullable=False)
    sharing = db.Column(MutableList.as_mutable(PickleType),
                                  default=[])
    price = db.Column(db.String(999))
    pre_advanced = db.Column(db.String(999),nullable=False)
    location = db.Column(db.String(999),nullable=False)
    g_location = db.Column(db.String(999), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    facilities = db.Column(MutableList.as_mutable(PickleType),
                                  default=[])
    pg_type = db.Column(db.String(999), nullable=False)
    room_type = db.Column(db.String(999), nullable=False)
    food_type = db.Column(db.String(999), nullable=False)
    photos = db.Column(db.String)
    bike_parking = db.Column(db.String(999),nullable=False)
    car_parking = db.Column(db.String(999),nullable=False)
    created_by = db.Column(db.String(999))
    updated_by = db.Column(db.String(999))
    client_name= db.Column(db.String(999))
    pincode = db.Column(db.String(999))


class User(db.Model):
    __bind_key__ = 'second'
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    firstname = db.Column(db.String(999),nullable=False)
    lastname = db.Column(db.String(999),nullable=False)
    email = db.Column(db.String(999),unique=True)
    password = db.Column(db.String(999),nullable=False)
    created_by = db.Column(db.String(999))


with app.app_context():
    db.create_all()



