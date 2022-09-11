from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from movielounge import app, db
from movielounge.models import Category, Users


# --- basic home app route ---#
@app.route("/")
def home():
    """
    renders base template
    """
    return render_template("base.html")


# --- Register page ---#
@app.route("/register")
def register():
    """
    Route for register.html and register form post
    """
    return render_template("register.html")
