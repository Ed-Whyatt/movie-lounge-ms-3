from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from movielounge import app, db, mongo, client
from movielounge.models import Category, Users


# --- Home app route displays all user movies --- #
@app.route("/")
@app.route("/get_movies")
def get_movies():
    """
    Gets movies from mongo database and displays them in the movie.html page
    """
    movies = mongo.db.movies.find()
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("movie.html", movies=movies, categories=categories)


# --- Get messgaes for message_board.html page --- #
@app.route("/get_questions")
def get_questions():
    """
    Gets all message questions and ancers and
    displayes them in message_bored.html
    """

    questions = (mongo.db.questions.find())
    answers = list(mongo.db.answers.find())
    return render_template(
        "message_board.html", questions=questions, answers=answers)


# --- Add a question to messge board --- #
@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    """
    Checks if user is loged in if not returns to message bord page,
    If the user is loged in then returns add question template then,
    Add the new question info from the form to the mongo database.
    """

    if "user" not in session:
        flash("You have to be loged in to add a message")
        return redirect("get_questions")

    if request.method == "POST":
        questions = {
            "category_name": request.form.get("category_name"),
            "question_description": request.form.get("question_description"),
            "created_by": session["user"]
        }
        mongo.db.questions.insert_one(questions)
        flash("Message Successfully Added")
        return redirect("get_questions")

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("add_question.html", categories=categories)


# --- Edit a question on message board --- #
@app.route("/edit_question/<question_id>", methods=["GET", "POST"])
def edit_question(question_id):
    """
    Checks if a user is loged in then,
    Gets the new message details from the form and edits the 
    message question in mongo database.
    """

    question = mongo.db.questions.find_one({"_id": ObjectId(question_id)})

    if "user" not in session:
        flash("You can only edit your own messages")
        return redirect(url_for("get_questions"))

    if request.method == "POST":
        submit = {
            "category_name": question.get("category_name"),
            "question_description": request.form.get("question_description"),
            "created_by": session["user"]
        }
        mongo.db.questions.replace_one({"_id": ObjectId(question_id)}, submit)
        flash("Message Successfully Updated")
        return redirect(url_for("get_questions"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template(
        "/edit_question.html", question=question, categories=categories)


# --- Delete a question on message board --- #
@app.route("/delete_question/<question_id>")
def delete_question(question_id):
    """
    Checks if user and the message created user is loged in then,
    Deletes the question message in the mongo database
    """

    if "user" not in session:
        flash("You can only delete your own message!")
        return redirect(url_for("get_questions"))

    mongo.db.questions.delete_one({"_id": ObjectId(question_id)})
    flash("Question Successfully Deleted")
    return redirect(url_for("get_questions"))


# --- Add a answer to a question on message board --- #
@app.route("/add_reply/<question_id>", methods=["GET", "POST"])
def add_reply(question_id):
    """
    Checks if user is loged in then, gets the information from the
    form for a new answer message and adds it to the mongo database.
    """
    answers = list(mongo.db.answers.find())
    question = mongo.db.questions.find_one({"_id": ObjectId(question_id)})

    if "user" not in session:
        flash("You need to be logged in to add a message")
        return redirect(url_for("get_questions"))

    if request.method == "POST":
        reply = {
            "answer_message": request.form.get("answer_message"),
            "question_id": question_id,
            "created_by": session["user"]
        }
        mongo.db.answers.insert_one(reply)
        flash("Message Successfully Added")
        return redirect(url_for("get_questions"))

    return render_template(
        "add_reply.html", question=question, answers=answers)


# --- Add movie search page page ---#
@app.route("/add_movie")
def add_movie():
    """
    Gets the add movie template witch contains search for a movie
    """
    if "user" not in session:
        flash("You need to be logged in to add a movie")
        return redirect(url_for("get_movies"))

    return render_template("add_movie.html")


# --- Movie Search --- #
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Gets the search query from the search form and searches 
    omdb("client") for movies, then passes them to the card
    in the rendered search_results.html template.
    """

    if "user" not in session:
        flash("You need to be logged in to add a movie")
        return redirect(url_for("get_questions"))

    # client is omdb search website and information,
    # documentation can be found at https://pypi.org/project/omdb/
    query = request.form.get("query")
    movies = client.search(query)
    return render_template("search_results.html", movies=movies)


# --- Select a movie to add to user list --- #
@app.route("/select_movie/<movie_title>", methods=["GET", "POST"])
def select_movie(movie_title):
    """
    Checks if a user is loged in then,
    Gets the movie tile from movie search results then,
    Adds search results and form data to the mongo movies database.
    """

    if "user" not in session:
        flash("You need to be logged in to add a movie")
        return redirect(url_for("get_movies"))

    movie = client.get(title=movie_title, fullplot=False, tomatoes=True)
    if request.method == "POST":
        task = {
            "category_id": request.form.get("category_id"),
            "user_rating": request.form.get("user_rating"),
            "user_notes": request.form.get("user_notes"),
            "title": movie.get("title"),
            "poster": movie.get("poster"),
            "director": movie.get("director"),
            "genre": movie.get("genre"),
            "actors": movie.get("actors"),
            "year": movie.get("year"),
            "type": movie.get("type"),
            "rated": movie.get("rated"),
            "imdb_rating": movie.get("imdb_rating"),
            "plot": movie.get("plot"),
            "created_by": session["user"]
        }
        mongo.db.movies.insert_one(task)
        flash("Movie Successfully Added")
        return redirect(url_for("get_movies"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template(
        "select_movie.html", categories=categories, movie=movie)


@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    """
    Checks if a user is loged in then,
    Gets the movie id from movie.html then,
    Replaces the new form data to mongo movies database.
    """

    if "user" not in session:
        flash("You need to be logged in to add a movie")
        return redirect(url_for("get_movies"))

    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})

    if request.method == "POST":
        submit = {
            "category_id": request.form.get("category_id"),
            "user_rating": request.form.get("user_rating"),
            "user_notes": request.form.get("user_notes"),
            "title": movie.get("title"),
            "poster": movie.get("poster"),
            "director": movie.get("director"),
            "genre": movie.get("genre"),
            "actors": movie.get("actors"),
            "year": movie.get("year"),
            "type": movie.get("type"),
            "rated": movie.get("rated"),
            "imdb_rating": movie.get("imdb_rating"),
            "plot": movie.get("plot"),
            "created_by": session["user"]
        }
        mongo.db.movies.replace_one({"_id": ObjectId(movie_id)}, submit)
        flash("Movie Successfully Updated")
        return redirect("/get_movies")

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template(
        "edit_movie.html", movie=movie, categories=categories)


@app.route("/delete_movie/<movie_id>")
def delete_movie(movie_id):
    """
    Gets movie id from movies list in movies.html then,
    Deletes the movie in the mongo movies database.
    """

    if "user" not in session:
        flash("You can only delete your own movie!")
        return redirect(url_for("get_movies"))

    mongo.db.movies.delete_one({"_id": ObjectId(movie_id)})
    flash("Movie Successfully Deleted")
    return redirect(url_for("get_movies"))


# --- admin get categories --- #
@app.route("/get_categories")
def get_categories():
    """
    Gets the categories and displays them for admin only
    """

    # check user admin is in session
    if session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("get_tasks"))

    # get categories list from database
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


# --- Add categories admin only --- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Checks the session user is admin then,
    Gets the new category name from the form and adds it to categories database
    """

    if session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("get_tasks"))

    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        flash("Category Added Successfully")
        return redirect(url_for("get_categories"))
    return render_template("add_category.html")


# --- edit categories --- #
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Checks if the admin user is in session then,
    Gets the updated category name from the form and replaces the category
    in the catorys database
    """

    if session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("get_tasks"))

    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        flash("Category Edit Successful")
        return redirect(url_for("get_categories"))
    return render_template("edit_category.html", category=category)


# --- delete categories admin only --- #
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    """
    Checks if the user is admin then,
    deletes selected catogory in the database
    """
    if session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("/get_tasks"))

    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    # need to add all links messages to this category
    flash("Category Deleted Successfully")
    return redirect(url_for("get_categories"))


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


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
