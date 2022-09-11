from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from movielounge import app, db
from movielounge.models import Category, Users


""" basic home app route """
@app.route("/")
def home():
    return render_template("base.html")
