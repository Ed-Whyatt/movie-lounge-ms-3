<h1 align="center">Movie Lounge</h1>

## A responsive movie lounge website hub for keen movie enthusiast.
***
## Code Institute – HTML, CSS, JavaScript, python+Flask and PostgreSQL -  Milestone Project 3.
***
## [Click Here To View The Live Project](https://movie-lounge-ms-3.herokuapp.com)
***
## ![Text](/documentation/i-am-responsive/i-am-responsive.png)
***
## UX user experience
***
## User stories
- ### First time user goals
    
    1. As a First time user, I want to easily navigate to register and then log in when first entering the website application.
    2. As a First Time User, I want to navigate the website easily and interact with the content.
    3. As a first time user i want to easily navigate to search for movies and add them to my list.
    4. As a first time user i want to easily navigate to the message board and add a message question or reply to a message.

- ### Returning user goals
    1. As a Returning User, I want to edit and delete my messages.
    2. As a Returning User, I want to edit and delete my movie list.
    3. As a Returning User, I want to see any new messages.
    4. As a Returning User, I want to see if anyone has replyed to my questions.

- ### Frequent user goals
    1. As a Frequent user, I want to easily reply to any messages or questions.
    2. As a Frequent user, I want to easily edit and delete my movie list.
    3. As a Frequent user, I want to easily edit or delete any messages or questions.

- ### End of user goals
    1. As a End of User, I want to delete all my messages and questions.
    2. As a End of User, I want to delete my movie list.

- ### Admin user goals
    1. As an Admin User, I want access to add questions and edit and delete  all questions on the movie lounge message board.
    2. As an Admin User, I want access to add movies and edit and delete all users movie lists.
    3. As an Admin User, I want access to add, edit and delete all categorys and related questions, messages and movie lists.


# Design

## Design Introduction
- This wbsite application is designed for users who are intrested in joinig the movie lounge comunity. Users will be able to search for movies and add there own commemts and ratings to them witch will be displayed on the home page. The users will be able to create questions and reply to them in on the message bored once they have created an accout and loged in. 

## Colour Scheme

- ### [Color Mind](http://colormind.io/) : Colormind has been used to aid the decision the colour scheme for the project.

### The main colours used in this website are:
- #### The main colours used for text and backgrounds:
### ![Text](/documentation/colours/colours.png)

## Typography:
- ### The fonts use throughout this website are:
    - Google fonts 'Lato'with a fallback of sans-serif.

## Imagery
- ### The main images used are from the omdb api and are used for the movie poster images and the links to the poster images are stored in the user movie database to display user movies. 
- ### The only image used from the movielounge static image folder is a placeholder image of popcorn for if an ondb poster image is not avaliable. The link to image of [popcorn](https://pixabay.com/photos/popcorn-food-carton-container-1085072/) is from [https://pixabay.com](https://pixabay.com).

## Wireframes

- ### Large screens

1. Welcome Home page Wireframe 
### ![text](/documentation/wireframes/enter_home_page.png)

2. Loged In Home Page Wireframe 
### ![text](/documentation/wireframes/loged_in_home.png)

3. Log In page Wireframe 
### ![text](/documentation/wireframes/log_in.png)

4. Register page Wireframe 
### ![text](/documentation/wireframes/register.png)

5. Message Board Wireframe page 
### ![text](/documentation/wireframes/message_board.png)

6. Add Movie and Search page wireframe 
### ![text](/documentation/wireframes/add_movie_search.png)

7. Select Movie to Add page wirframe 
### ![text](/documentation/wireframes/select_movie.png)

8. Manage Categories page (admin only ) wirframe
### ![text](/documentation/wireframes/manage_categories.png)

- ### Medium Screens click to view

1. Medium Welcome Home page Wireframe [view](/documentation/wireframes/enter_home_medium.png)
2. Medium Loged In Home Page Wireframe [view](/documentation/wireframes/loged_in_home_medium.png)
3. Medium Log In page Wireframe [view](/documentation/wireframes/log_in_medium.png)
4. Medium Register page Wireframe [view](/documentation/wireframes/register.png)
5. Medium Message Board Wireframe page [view](/documentation/wireframes/message_board_medium.png)
6. Medium Add Movie and Search page wireframe [view](/documentation/wireframes/add_movie_medium.png)
7. Medium Select Movie to Add page wirframe [view](/documentation/wireframes/select_movie_medium.png)
8. Medium Manage Categories page  (admin only ) wirframe [view](/documentation/wireframes/category_medium.png)

- ### Small Screens click to view
1. Small Welcome Home page Wireframe [view](/documentation/wireframes/enter_home_small.png)
2. Small Loged In Home Page Wireframe [view](/documentation/wireframes/loged_in_home_small.png)
3. Small Log In page Wireframe [view](/documentation/wireframes/log_in_small.png)
4. Small Register page Wireframe [view](/documentation/wireframes/register_small.png)
5. Small Message Board Wireframe page [view](/documentation/wireframes/message_board_small.png)
6. Small Add Movie and Search page wireframe [view](/documentation/wireframes/add_movie_small.png)
7. Small Select Movie to Add page wirframe [view](/documentation/wireframes/select_movie_small.png)
8. Small Manage Categories page  (admin only ) wirframe [view](/documentation/wireframes/category_small.png)

# Data Structure
- [Mongo DB](https://www.mongodb.com/) is a cloud based storage application, hosting storage for the user movie, messages and message reply data for 
 Movie Lounge.
- [PostgreSQL](https://www.postgresql.org/) is used for the backend functionality of the application, that allows admin to crate categorys and users to register and log in to the Movie Lounge.

## Data Model
# ![text](/documentation/data_model/data-model.png)

- User collection
   - This collection holds the user name and passwords for the Movie Lounge application.
   - The user collection user name links this collection to the movie, question, and anwswers collections user created by. This will show witch user has created each input into the collectins.

- Category collection
    - This collection holds the category names and can only be changed by admin.
    - The category collection category name links to questions and movies collection category name. This will show witch category the user has selected for each input into the collections.

- Movies collection
    - This collection holds the users movies information to be displayed in the Movie Lounge application.
    - The movies collection category name links to the category category name and the user created by links to the user collections. This will show with user and category the user has selected for each movie input into the movies collections.

- Question collection
    - This collection holds the users messages to be displayed in the Movie Lounge application message board.
    - The question collection user created by links to the user user name collecton. This will show witch user has input the message in the movie lounge message board.
    - The question collection id links to the answers collection question id. This will show witch answers link to the message in the movie loubge message board.   

- Answers collection
    - This collection hols the users answers to the messages to be displayed in the movie lounge application message board.
    - The answers question id links to the questions id. This will show witch message the user is replying to in the movie lounge message board. 

# Features
Am I Responsive has been used for the responsive image at the top of README.md you can view there website below and interact with this project on each device.
-   ### Responsive on all devices - [view](https://ui.dev/amiresponsive?url=https://movie-lounge-ms-3.herokuapp.com)

## Interactive elements.
- Navgation
    - Navgation on large screens
    ### ![text](/documentation/introactive-images/nav.png)
    - Navgation on small screens
    ### ![text](/documentation/introactive-images/nav-small.png)
    - Navagation small screens open
    ### ![text](/documentation/introactive-images/nav-small-open.png)
- Footer
    - Links to social media
    ### ![text](/documentation/introactive-images/footer.png)
- Home screen
    - Movie edit and delete user movies
    ### ![text](/documentation/introactive-images/movie-info-before.png)
    - Movie view more information
    ### ![text](/documentation/introactive-images/movie-info-after.png)
    - Movie edit page
    ### ![text](/documentation/introactive-images/edit-movie.png)
    - Movie delete modal
    ### ![text](/documentation/introactive-images/del-movie-modal.png)
- Message board
    - Add, Reply and Edit Delete question
    ### ![text](/documentation/introactive-images/add-edi-del-msg.png)
    - Add questioin page
    ### ![text](/documentation/introactive-images/add-msg.png)
    - Edit question page
    ### ![text](/documentation/introactive-images/edit-msg-page.png)
    - Delete question modal
    ### ![text](/documentation/introactive-images/del-msg-modal.png)
     - View, edit and delete replies
    ### ![text](/documentation/introactive-images/msg-reply-open.png)
    - Add replys
    ### ![text](/documentation/introactive-images/mas-reply-page.png)
    - Edit reply page
    ### ![text](/documentation/introactive-images/edit-reply-msg.png)
    - Delete reply message modal
    ### ![text](/documentation/introactive-images/del-reply-modal.png)
- Add Movie
    - Movie search
    ### ![text](/documentation/introactive-images/movie-search.png)
    - Movie search results select movie
    ### ![text](/documentation/introactive-images/movie-results.png)
    - Add movie selected
    ### ![text](/documentation/introactive-images/movie-add.png)
- Manage categorys
    - Add Edit Delete categorys
    ### ![text](/documentation/introactive-images/add-cat.png)
    - Add category page
    ### ![text](/documentation/introactive-images/add-a-cat.png)
    - Edit category page
    ### ![text](/documentation/introactive-images/edit-cat.png)
    - Delete category modal
    ### ![text](/documentation/introactive-images/del-cat.png)
- Log in
   ### ![text](/documentation/introactive-images/login.png)
- Register
   ### ![text](/documentation/introactive-images/register.png)
- User loged in display name
    - User loged in
    ### ![text](/documentation/introactive-images/user-loged-in.png)
    - User not loged in
    ### ![text](/documentation/introactive-images/login-msg.png)

## Technologies Used
### Languages Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://www.python.org/)

### Frameworks libraries and programming interface
1. [Bootstrap 5.2.0:](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts is used to import the Google font 'Lato' with a fallback of sans-serif into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes.
1. [Am I Responsive Design:](http://ami.responsivedesign.is/)
    - Am I Responsive Design was used for the responsive image in Readme.
1. [Pymongo](https://pypi.org/project/pymongo/) and [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - To connect Python and Flask to the MongoDB databame.
1. [Flask](https://flask.palletsprojects.com/en/2.2.x/)
    - To construct and render page templates, and create an instance of the app itself.
1. [MongoDB Atlas](https://www.mongodb.com/)
    - A cloud-based Non-Relational backend database hosting service.
1. [WerKzeug](https://werkzeug.palletsprojects.com/en/2.2.x/)
    - A WSGI web application library used for hashing user passwords for Python.
1. [jinja](https://jinja.palletsprojects.com/en/3.1.x/)
    - Templating language for Python, to simplify displaying data from the backend of this project smoothly and effectively in HTML.
1. [SQLAlchemy](https://www.sqlalchemy.org/)
    - Used to filter and search through the database.
1. [omdb.py](https://omdbpy.readthedocs.io/en/latest/)
    - Python wrapper around The Open Movie Database API (OMDb API): [http://omdbapi.com/](http://omdbapi.com/). Used for the movie search.
1. [Heroku](https://id.heroku.com/login)
    - A cloud based platform for that is used for hosting this python web based aplication. 

***
## Testing

### Testing is in TESTING.md - [Link to TESTING.md](#) NO LINK
***

## Deployment
***

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Ed-Whyatt/movie-lounge-ms-3.git)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Ed-Whyatt/movie-lounge-ms-3.git)
2. Under the repository name, click "<> Code" and click the second "code" dropdown menu. 
3. To clone the repository using HTTPS, click the second "code ▼" dropdown menu, copy the link [HTTPS link](https://github.com/Ed-Whyatt/movie-lounge-ms-3). NO LINK
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

$ git `clone https://github.com/Ed-Whyatt/movie-lounge-ms-3.git`

7. Press Enter. Your local clone will be created.

```bash
git clone https://github.com/Ed-Whyatt/movie-lounge-ms-3.git
Cloning into CI-Clone...
remote: Counting objects: 10, done.
remote: Compressing objects: 100% (8/8), done.
remove: Total 10 (delta 1), reused 10 (delta 1)
Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/Ed-Whyatt/movie-lounge-ms-3.git)

***

## Setting up MongoDB Atlas for database use

You will need to go to MonGoDB Atlas and create an accout first, Details on how to do this can be found here: [MongoDB Atlas](https://www.mongodb.com/docs/atlas/)

1. Once you have loged in navgate click to create a cluster.
2. Select a clound service aws is free and used for this database.
3. Select the region that is nearest to you e.g Europe (Ireland).
4. Select cluster Tier M0 has been used for this site and is free.
5. Scroll down to the bottom and choose a cluster name e.g. movielounge, This will be used in your own env.py with your own vars and keys witch will never be stored in your git hub repo.
6. Then click on create cluster. This will take a few minits to create your Database and take you to your database page.
7. Click on Database Access, Then Add New Database User.
8. Create a new user and password do not use non-alphanumeric characters (e.g.: ?, %,@ or &) in your username or password! Make sure your user privileges are set to Read and Write to any database.
9. Then click add user.
10. Next click on Network Access and add the IP address you will use to access your database.
10, Click on clusters tab and select your cluster e.g. My First Cluster.
11. Then select collections tab and click on Add My Own Data.
12. Fill out the new database name e.g Database name - myFirstDB , Collection name - movies, questions and ancers. Then click create.
13. Once you have created the databases click on insert document and fill in the details for each database. The databases for the three mongo database documents used for this project are:
### - answers
![text](/documentation/mongo-db-documents-images/answers.png)
### - questions
![text](/documentation/mongo-db-documents-images/questions.png)
### - movies
![text](/documentation/mongo-db-documents-images/movies.png)

***

## Setting up Flask Development env.py file with vars and keys for mongo database, prosgres database and omdb api wrapper.

1. First navigate to [http://www.omdbapi.com/](http://www.omdbapi.com/) select the api key tab and fill in the form to recive your ondb via email. this will go in the env.py file shown in step 7.
2. Open the terminal in your gitpod workspace.
3. To istall the framworks to work with progress database and omdb wrapper type in the terminal:
```bash
pip3 install Flask-SQLAlchemy psycopg2 omdb
```
4. Next, we will be storing some sensitive data, and we need to hide them using environment variables hidden within a new file called 'env.py'.
5. Create a new env.py in the terminal by typeing:
```bash
touch env.py
```
6. Make sure yo have a '.gitignore' if not create one and that env.py is in the list so that this will not be pushed to your git hub repo.
```bash
touch .gitignore
```
7. Within your env.py file put in the following with your relevent keys information.
```python
import os

os.environ.setdefault("IP", "e.g. 0.0.0.0")
os.environ.setdefault("PORT", "e.g. 5000")
os.environ.setdefault("SECRET_KEY", "your_own_secret_key")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgresql:/// name of your database here ")
os.environ.setdefault("MONGO_URI", " name of your mongo uri here")
os.environ.setdefault("MONGO_DBNAME", " your mongo database name")
os.environ.setdefault("API_KEY", " your omdb key here ")
```
9. Next create a folder for your app e.g. movielounge and within that folder create a ```__init__.py``` This will make sure to initialize our taskmanager application as a package, allowing us to use
our own imports, as well as any standard imports.
```bash
__init__.py
```
10. 
- Now we can create an instance of the imported Flask() class, and that will be stored in
a variable called 'app', which takes the default Flask __name__ module.
Then, we need to specify two app configuration variables, and these will both come from our environment variables.
app.config SECRET_KEY and app.config SQLALCHEMY_DATABASE_URI, both wrapped in square brackets and quotes.
Each of these will be set to get their respective environment variable, which is SECRET_KEY,
and the short and sweet DB_URL for the database location which we'll set up later.
Then, we need to create an instance of the imported SQLAlchemy() class, which will be
assigned to a variable of 'db', and set to the instance of our Flask 'app'.

- Finally, from our movielounge package, we will be importing a file called 'routes' which is allready create in the movie-lounge-ms-3 repo. 
- Within your ```__init__.py``` file should look like the following.

```python
import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from omdb import OMDBClient
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["API_KEY"] = os.environ.get("API_KEY")


db = SQLAlchemy(app)
mongo = PyMongo(app)
api_key = os.environ.get("API_KEY")
client = OMDBClient(apikey=api_key)

from movielounge import routes  # noqa

```
11. Now it's time to create the main Python file that will actually run the entire application.
This will be at the root level of our workspace, not part of the movielounge package itself.
Since it will run the whole application, let's just call it run.py in that case.
```bash
touch run.py
```
12. Use the same details located in the movie-lounge-ms-3 repo run.py file.
```python
import os
from movielounge import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

```
***
Setting up Prosgres local Database
***
Using the models.py file in the movie-lounge-ms-3 repo. This file will create the Users and Categorys in the posgress database.
- models.py file
```python
from movielounge import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Users(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name
```
1. Open the terminal in your gitpod workspace and type the following and hit enter.
```bash
set_pg
```
2. Then
```bash
psql
```
You should see the follwing:
```psql
psql (12.12 (Ubuntu 12.12-1.pgdg20.04+1))
Type "help" for help.

postgres=# 
```
3. To create the database type the follwing and hit enter:
```psql
postgres=# CREATE DATABASE movielounge;
```
4. To check it has worked type
```psql
postgres=# \c movielounge;
```
- You should now see the new psql movielounge database in the cli as follows.
```psql
movielounge=#
```
5. Now exit psql cli by typing \q and hit enter.
```psql 
movielounge=#\q
```
6. Next, we need to use Python to generate and migrate our models into this new database.
This will take the models that we've created for Category and Users, and build the database schema using the details we've provided.
By typing python3 enter in the gitpod workspace terminal.
```bash
python3
```
- you shold now be in the python interpreter
```psql
Python 3.8.11 (default, Sep  7 2022, 11:13:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
````
7. From here, we need to import our 'db' variable found within the movielounge package, so type:
from movielounge import db
```psql
Python 3.8.11 (default, Sep  7 2022, 11:13:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from movielounge import db
````
8. Now, using db, we need to perform the .create_all() method:
```psql
Python 3.8.11 (default, Sep  7 2022, 11:13:18) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from movielounge import db
>>> db.create_all()
````
9. That's it, pretty simple enough, our Postgres database should be populated with these two tables and their respective columns and relationships.
10. Type exit() to exit the python interpreter.
```psql
>>> exit()
````
11. Finaly to check everything worked you can check the psql movielounge by typing.
```psql
psql -d movielounge
```
- Then type
```psql
\dt
```
- You should see the tables and there relevent collums.
```psql
psql (12.12 (Ubuntu 12.12-1.pgdg20.04+1))
Type "help" for help.
movielounge-# \dt
         List of relations
 Schema |   Name   | Type  | Owner  
--------+----------+-------+--------
 public | category | table | gitpod
 public | users    | table | gitpod
(2 rows)

movielounge-# 
```

## Deployment on Heroku and linking git repo

## Credits
***

###  Code

   -   [Code Institute](https://codeinstitute.net/): Code Institutes lessons have help with all coding throughout this project.

   -   [Code Institute Sample README.md](https://github.com/Code-Institute-Solutions/SampleREADME): Code Institute Sample README.md has been used to help with readme layout.

   -   [Bootstrap5](https://getbootstrap.com/docs/5.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

   -   [W3 Schools](https://www.w3schools.com/): W3 Schools has been used with some elements in this project.


   -   OTHERS
   -
   -

 - ### Tutorials used
    - ####  DOCUMTATION FOR OMDB
   


### Content
   -   All content was written by the developer.

### Acknowledgments

   -	My mentor for continuous helpful feedback.
   -	Tutor support at Code Institute.
   -	Support from staff at The City of Bristol collage.
   -	Members on Code Institutes Slack.
