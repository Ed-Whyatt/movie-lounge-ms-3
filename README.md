git <h1 align="center"> Movie Lounge</h1>

## A responsive movie lounge website hub for keen movie enthusiast.
***
## Code Institute – HTML, CSS, JavaScript, python+Flask and PostgreSQL -  Milestone Project 3.
***
## [Click Here To View The Live Project](#) NO LINK
***
## ![Text](#) - responsive image here NO LINK
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
    4. As a Returning User, I want to see any new messages.
    5. As a Returning User, I want to see if anyone has replyed to my questions.

- ### Frequent user goals
    1. As a Frequent user, I want to easily reply to any messages or questions.
    2. As a Frequent user, I want to easily edit and delete my movie list.
    3. As a Frequent user, I want to easily change my password.
    4. As a Frequent user, I want to easily edit or delete any messages or questions.

- ### End of user goals
    1. As a End of User, I want to delete my login details
    2. As a End of User, I want to delete all my messages and questions.
    3. As a End of User, I want to delete my movie list.

- ### Admin user goals
    1. As an Admin User, I want access to add questions and edit and delete  all questions on the movie lounge message board.
    2. As an Admin User, I want access to add movies and edit and delete all users movie lists.
    3. As an Admin User, I want access to add, edit and delete all categorys and related questions, messages and movie lists.


# Design

## Design Introduction
- 
## Colour Scheme

- ### [Color Mind](http://colormind.io/) : Colormind has been used to aid the decision the colour scheme for the project.

### The main colours used in this website are:
- 
- #### The main colours used for text and backgrounds:
### ![Text](#) NO LINK

## Typography:
- ### The fonts use throughout this website are:
    - 

## Imagery

## Wireframes

- ### Large screens

1. Welcome Home page Wireframe ![text](#)

2. Loged In Home Page Wireframe ![text](#)

3. Log In page Wireframe ![text](#)

4. Reginster page Wireframe ![text](#)

5. Message Board Wireframe page ![text](#)

6. Add Movie and Search page wireframe ![text](#)

7. Select Movie to Add page wirframe ![text](#)

8. Manage Categories page  (admin only ) wirframe ![text](#)

- ### Medium Screens click to view

1. Medium Welcome Home page Wireframe ![view](#)
2. Medium Loged In Home Page Wireframe ![view](#)
3. Medium Log In page Wireframe ![view](#)
4. Medium Reginster page Wireframe ![view](#)
5. Medium Message Board Wireframe page ![view](#)
6. Medium Add Movie and Search page wireframe ![view](#)
7. Medium Select Movie to Add page wirframe ![view](#)
8. Medium Manage Categories page  (admin only ) wirframe ![view](#)

- ### Small Screens click to view
1. Small Welcome Home page Wireframe ![view](#)
2. Small Loged In Home Page Wireframe ![view](#)
3. Small Log In page Wireframe ![view](#)
4. Small Reginster page Wireframe ![view](#)
5. Small Message Board Wireframe page ![view](#)
6. Small Add Movie and Search page wireframe ![view](#)
7. Small Select Movie to Add page wirframe ![view](#)
8. Small Manage Categories page  (admin only ) wirframe ![view](#)

# Data Structure
- [Mongo DB](https://www.mongodb.com/) is a cloud based storage application, hosting storage for the user movie, messages and message reply data for 
 Movie Lounge.
- [PostgreSQL](https://www.postgresql.org/) is used for the backend functionality of the application, that allows admin to crate categorys and users to register and log in to the Movie Lounge.

## Data Model
# ![text](#)

- User collection
   - This collection holds the user name and passwords for the Movie Lounge application.
   - The user collection user name links this collection to the movie, question, and anwswers collections user created by. This will show witch user has created each input into the collectins.

- Category collection
    - This collection holds the category names and can only be changed by admin.
    - The category collection category name links to questions and movies collection category name. This will show witch category the user has selected for each input into the collections.

- Movies colection
    - This collection holds the users movies information to be displayed in the Movie Lounge application.
    - The movies collection category name links to the category category name and the user created by links to the user collections. This will show with user and category the user has selected for each movie input into the movies collections.

- Question colection
    - This collection holds the users messages to be displayed in the Movie Lounge application message board.
    - The question collection user created by links to the user user name collecton. This will show witch user has input the message in the movie lounge message board.
    - The question collection id links to the answers collection question id. This will show witch answers link to the message in the movie loubge message board.   

- Answers colection
    - This collection hols the users answers to the messages to be displayed in the movie lounge application message board.
    - The answers question id links to the questions id. This will show witch message the user is replying to in the movie lounge message board. 

# Features
Am I Responsive has been used for the responsive image at the top of README.md you can view there website below and interact with this project on each device.
-   ### Responsive on all devices - [view](#) NO LINK

## Interactive elements.
- Interactive elements

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
    - Google fonts were used to import the 'Lato', 'Poppins' and 'Pacifico' fonts into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes
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
    - Python wrapper around The Open Movie Database API (a.k.a. OMDb API): [http://omdbapi.com/](http://omdbapi.com/). Used for the movie search.

###  keys: 
-
 #### Creating keys

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


## Credits
***

###  Code

   -   [Code Institute](https://codeinstitute.net/): Code Institutes lessons have help with all coding throughout this project.

   -   [Code Institute Sample README.md](https://github.com/Code-Institute-Solutions/SampleREADME): Code Institute Sample README.md has been used to help with readme layout.

   -   [Bootstrap5](https://getbootstrap.com/docs/5.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

   -   [W3 Schools](https://www.w3schools.com/): W3 Schools has been used with some elements in this project.

   -   [Autoprefixer](https://autoprefixer.github.io/): Autoprefixer has been used with the images in css for Crapple/Apple/iOS fallback browsers.

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
