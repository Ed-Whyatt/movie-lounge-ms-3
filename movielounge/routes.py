from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from movielounge import app, db
from movielounge.models import Category, Users


# --- basic home app route ---#
@app.route("/")
@app.route("/get_movies")
def get_movies():
    """
    renders home page template that will show users movies
    """
    return render_template("movie.html")


# --- Register page ---#
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Gets register.html template and form to Post,
    then adds the details to the User db
    """
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).all()

        if existing_user:
            flash("Usernmae already exists")
            return redirect(url_for("register"))

        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_movies"))

    return render_template("register.html")


# --- Log In page --- #
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Gets login.html template and form to Post,
    then checks if user is loged in the session
    then logs them into session.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(Users.user_name == request.form.get(
            "username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(existing_user[0].password, request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_movies"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")
