from flask import Blueprint, flash, render_template, url_for, redirect, request, session
from apps.user.models import *

user = Blueprint("user", __name__, template_folder="templates")


@user.route("/")
def index():
    users = User.query.order_by(User.created_at).all()

    return render_template("index.html", users=users)


@user.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    else:
        data = User(
            email=request.form["email"],
            password=User.set_password(request.form["password"]),
        )
        db.session.add(data)
        db.session.commit()

        flash("Data added successfully", "success")

    return redirect(url_for("user.index"))


@user.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    user = User.query.get(id)

    if request.method == "GET":
        return render_template("edit.html", user=user)

    if request.method == "POST":
        user.email = request.form["email"]
        user.password = User.set_password(request.form["password"])
        db.session.commit()

        flash("berhasil diupdate", "success")

    return redirect(url_for("user.index"))


@user.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    if request.method == "GET":
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        flash("dihapus", "success")

    return redirect(url_for("user.index"))
