<h1 align="center"> Movie Lounge</h1>

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

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
