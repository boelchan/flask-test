from database.database import db


class Orang(db.Model):
    __tablename__ = "orang"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200))
    alamat = db.Column(db.String(200))
    tanggal_lahir = db.Column(db.Date())

    kontaks = db.relationship("Kontak", cascade="all", backref="orang")


class Provider(db.Model):
    __tablename__ = "provider"
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))


class Kontak(db.Model):
    __tablename__ = "kontak"
    id = db.Column(db.Integer, primary_key=True)
    orang_id = db.Column(db.Integer(), db.ForeignKey(Orang.id))
    provider_id = db.Column(db.Integer(), db.ForeignKey(Provider.id))
    nomer = db.Column(db.String(50))

    provider = db.relationship("Provider", backref="kontak")

    @property
    def nomerHp(self):
        return self.provider.nama + " " + self.nomer
