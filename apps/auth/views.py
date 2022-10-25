from flask import Blueprint, flash, render_template, url_for, redirect, request, session

from apps.user.models import User

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user and user.check_password(request.form["password"]):
            flash("login berhasil", "success")
            session["logged_in"] = True

            return redirect(url_for("user.index"))

        flash("user salah", "danger")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("logout berhasil", "info")

    return redirect(url_for("user.index"))
