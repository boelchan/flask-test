from flask import Blueprint, flash, render_template, url_for, redirect, request, session

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (
            request.form["email"] == "superadmin@app.com"
            and request.form["password"] == "123"
        ):
            flash("login berhasil", "success")
            session["logged_in"] = True

            return redirect(url_for("crud.index"))

    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("logout berhasil", "info")

    return redirect(url_for("crud.index"))
