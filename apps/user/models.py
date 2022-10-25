from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import func
from database.connection import db


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )


class User(Base):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(250))
    last_login = db.Column(db.DateTime())

    contacts = db.relationship("Contact", cascade="all", backref="user")

    def __init__(self, password, email):
        self.email = email
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password, method="pbkdf2:sha1")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def refresh_last_login(self):
        self.last_login = datetime.now()


class Provider(Base):
    __tablename__ = "provider"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))


class Contact(Base):
    __tablename__ = "contact"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    provider_id = db.Column(db.Integer(), db.ForeignKey(Provider.id))
    nomer = db.Column(db.String(50))

    provider = db.relationship("Provider", backref="contact")

    @property
    def nomerHp(self):
        return self.provider.nama + " " + self.nomer
