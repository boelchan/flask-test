from datetime import datetime
from database.connection import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(250))
    last_login = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(
        db.DateTime(), default=datetime.now(), onupdate=datetime.now()
    )
    contacts = db.relationship("Contact", cascade="all", backref="user")

    def set_password(password):
        return generate_password_hash(password, method="pbkdf2:sha1")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def refresh_last_login(self):
        self.last_login = datetime.now()
        db.session.commit()


class Provider(db.Model):
    __tablename__ = "provider"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(
        db.DateTime(), default=datetime.now(), onupdate=datetime.now()
    )


class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    provider_id = db.Column(db.Integer(), db.ForeignKey(Provider.id))
    nomer = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(
        db.DateTime(), default=datetime.now(), onupdate=datetime.now()
    )

    provider = db.relationship("Provider", backref="contact")

    @property
    def nomerHp(self):
        return self.provider.nama + " " + self.nomer
