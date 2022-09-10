from flask import flash, render_template, request, redirect, session, url_for
from movielounge import app, db


@app.route("/")
def home():
    return render_template("base.html")
