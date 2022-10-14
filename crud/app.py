from flask import Flask, flash, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_test'
db = SQLAlchemy(app)


class Orang(db.Model):
    __tablename__ = "orang"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200))
    alamat = db.Column(db.String(200))
    tanggal_lahir = db.Column(db.Date())

    def __init__(self, nama, alamat, tanggal_lahir):
        self.nama = nama
        self.alamat = alamat
        self.tanggal_lahir = tanggal_lahir


@app.route('/')
def index():
    orangs = Orang.query.all()

    return render_template('index.html', orangs=orangs)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        nama = request.form['nama']
        alamat = request.form['alamat']
        tanggal_lahir = request.form['tanggal_lahir']

        data = Orang(nama, alamat, tanggal_lahir)
        db.session.add(data)
        db.session.commit()

        flash('Data added successfully', 'success')

        return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    orang = Orang.query.get(id)

    if request.method == 'GET':
        return render_template('edit.html', orang=orang)

    if request.method == 'POST':
        orang.nama = request.form['nama']
        orang.alamat = request.form['alamat']
        orang.tanggal_lahir = request.form['tanggal_lahir']
        db.session.commit()

        flash('berhasil diupdate', 'success')

        return redirect(url_for('index'))

    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    if request.method == 'GET':
        orang = Orang.query.get(id)
        db.session.delete(orang)
        db.session.commit()

        flash('dihapus', 'success')

        return redirect(url_for('index'))

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['email'] == 'superadmin@app.com' and request.form['password'] == '123':
            flash('login berhasil', 'success')
            session['logged_in'] = True

            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('logout berhasil', 'info')

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
