from flask import Blueprint, flash, render_template, url_for, redirect, request, session
from apps.crud.models import *

crud = Blueprint("crud", __name__, template_folder="templates")


@crud.route("/")
def index():
    orangs = Orang.query.order_by(Orang.tanggal_lahir).all()

    return render_template("index.html", orangs=orangs)


@crud.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    else:
        nama = request.form["nama"]
        alamat = request.form["alamat"]
        tanggal_lahir = request.form["tanggal_lahir"]

        data = Orang(nama, alamat, tanggal_lahir)
        db.session.add(data)
        db.session.commit()

        flash("Data added successfully", "success")

        return redirect(url_for("index"))


@crud.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    orang = Orang.query.get(id)

    if request.method == "GET":
        return render_template("edit.html", orang=orang)

    if request.method == "POST":
        orang.nama = request.form["nama"]
        orang.alamat = request.form["alamat"]
        orang.tanggal_lahir = request.form["tanggal_lahir"]
        db.session.commit()

        flash("berhasil diupdate", "success")

        return redirect(url_for("index"))

    return redirect(url_for("index"))


@crud.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    if request.method == "GET":
        orang = Orang.query.get(id)
        db.session.delete(orang)
        db.session.commit()

        flash("dihapus", "success")

        return redirect(url_for("index"))

    return redirect(url_for("index"))


@crud.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (
            request.form["email"] == "superadmin@app.com"
            and request.form["password"] == "123"
        ):
            flash("login berhasil", "success")
            session["logged_in"] = True

            return redirect(url_for("index"))

    return render_template("login.html")


@crud.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("logout berhasil", "info")

    return redirect(url_for("login"))
