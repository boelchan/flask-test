from flask import Flask, flash, render_template, url_for, redirect, request, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask_test'
mysql = MySQL(app)


@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM orang ''')
    orangs = cursor.fetchall()
    cursor.close()

    return render_template('index.html', orangs=orangs)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        nama = request.form['nama']
        alamat = request.form['alamat']
        tanggal_lahir = request.form['tanggal_lahir']

        cursor = mysql.connection.cursor()
        cursor.execute(
            '''INSERT INTO orang(nama,alamat,tanggal_lahir) VALUES(%s,%s,%s)''', (nama, alamat, tanggal_lahir))
        mysql.connection.commit()
        flash('Data added successfully', 'success')
        cursor.close()

        return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM orang WHERE id=%s''', (id,))
        orang = cursor.fetchone()
        cursor.close()

        return render_template('edit.html', orang=orang)

    if request.method == 'POST':
        nama = request.form['nama']
        alamat = request.form['alamat']
        tanggal_lahir = request.form['tanggal_lahir']

        cursor = mysql.connection.cursor()
        cursor.execute(''' 
        UPDATE orang 
        SET 
            nama = %s,
            alamat = %s,
            tanggal_lahir = %s
        WHERE
            id = %s;
        ''', (nama, alamat, tanggal_lahir, id))

        mysql.connection.commit()
        cursor.close()

        flash('berhasil diupdate', 'success')

        return redirect(url_for('index'))

    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' DELETE FROM orang WHERE id=%s''', (id, ))
        mysql.connection.commit()
        cursor.close()

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
