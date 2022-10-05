# Testing

## pep8
***
[pep8online.com](https://pep8online.com) has been used throughout the development of this application to test that the python code is pep8 compliant. At the writing  and testing of this app pep8online.com is currently down.
As a workaround, PEP8 validator has been added to the GitPod Workspace directly by following these steps:
1. Run the command pip3 install pycodestyle  Note that this extension may already be installed, in which case this command will do nothing.
2. In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
3. Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results (image 1).
4. Select pycodestyle from the list (image 2).
5. PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.
- Image 1
#### ![text](/documentation/pep8/pep8-walkaround/pep8-image-1.png)
- Image 2
#### ![text](/documentation/pep8/pep8-walkaround/pep-8-image-2.png)
- Image 3
#### ![text](/documentation/pep8/pep8-walkaround/pep8-image-3.png)

### PEP8 Results
- ```__init__.py```
#### ![text](/documentation/pep8/pep8-images/init-pep8.png)
- ```models.py```
#### ![text](/documentation/pep8/pep8-images/models.png)
- ```routes.py```
#### ![text](/documentation/pep8/pep8-images/routes.png)
- ```run.py```
#### ![text](/documentation/pep8/pep8-images/run.png)


## W3C Markup Validator [link](https://validator.w3.org/#validate_by_uri)
***
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
All pages have been checked with the base page active for meta data to be loaded for errors.
- Base html used for main navigation and footer on all pages base.html.
### ![text](/documentation/w3-validator/base.png)
- Add category page add_category.html
### ![text](/documentation/w3-validator/add-cat.png)
- Add movie search page add_movie.html
### ![text](/documentation/w3-validator/add-movie.png)
- Add a question for the message board questions add_questuion.html
### ![text](/documentation/w3-validator/add-question.png)
- Add a reply to the question on the message board add_reply.html
### ![text](/documentation/w3-validator/add-reply.png)
- Categories view categories.html
### ![text](/documentation/w3-validator/categories.png)
- Edit categories edit_category.html
### ![text](/documentation/w3-validator/edit-cat.png)
- Edit movie page edit_movie.html
### ![text](/documentation/w3-validator/edit-movie.png)
- Edit question page edit_question.html
### ![text](/documentation/w3-validator/edit-question.png)
- Edit reply edit_reply.html
### ![text](/documentation/w3-validator/edit-reply.png)
- Login page login.html
### ![text](/documentation/w3-validator/login.png)
- Message board displays the message questions and replies message_board.html
### ![text](/documentation/w3-validator/message-board.png)
- Movie page witch is the home page displaying users movies movie.html
### ![text](/documentation/w3-validator/movie.jpg)
- Register page register.html
### ![text](/documentation/w3-validator/register.png)
- Search results that displays the add movie search results search_results.html
### ![text](/documentation/w3-validator/search-results.png)
- Selected movie that displays the selected movie for a user to add to their list select_movie.html
### ![text](/documentation/w3-validator/select-movie.png)
- Error 404.html
### ![text](/documentation/error-pages/404-val.png)
- Error 500.html
### ![text](/documentation/error-pages/500-val.png)

### w3c CSS [link](https://jigsaw.w3.org/css-validator/#validate_by_input)
- CSS style.css
### ![text](/documentation/w3-validator/w3c-css-validator.png)

***
## Google Chrome Developer Tools
***
Google Chrome Developer Tools has been used throughout the development of this page, To use it in Google Crome browser Right click anywhere on the screen and click inspect on the menu then select lighthouse.

### Google Chrome Developer Tool Lighthouse results
- Home page
    - Before bugs fixed details in bugs section below.
   ### ![text](/documentation/dev-lighthouse/home-page-lh/home-page-before.png)
    - After bugs fixed.
        ### ![text](/documentation/dev-lighthouse/home-page-lh/home-page-lh-after.png)
- Edit movie page
### ![text](/documentation/dev-lighthouse/edit-movie-lh.png)
- Message board page
### ![text](/documentation/dev-lighthouse/message-bord-lh.png)
- Message board add question page
### ![text](/documentation/dev-lighthouse/add-question.png)
- Message board edit question page
### ![text](/documentation/dev-lighthouse/edit-question-lh.png)
- Message board add reply to question page
### ![text](/documentation/dev-lighthouse/question-reply-lh.png)
- Message board edit reply message
### ![text](/documentation/dev-lighthouse/edit-reply-lh.png)
- Add movie search and search results page
### ![text](/documentation/dev-lighthouse/add-movie-lh.png)
- Select movie page
### ![text](/documentation/dev-lighthouse/select-movie-lh.png)
- Manage categories
### ![text](/documentation/dev-lighthouse/categories-lh.png)
- Add category
### ![text](/documentation/dev-lighthouse/add-cat-lh.png)
- Edit category
### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-lh-after.png)
- Login
### ![text](/documentation/dev-lighthouse/login-lh.png)
- Register
### ![text](/documentation/dev-lighthouse/register-lh.png)
***
### Bugs Fixed
***
## Google dev tool lighthouse highlighted bugs.
- Home page
    - Dev tools highlighted modal aria ids and element order which have been fixed by adding loop-index to modal ids and aria attributes.
    ### ![text](/documentation/dev-lighthouse/home-page-lh/home-lh-aria-bug.png)
    ### ![text](/documentation/dev-lighthouse/home-page-lh/heme-page-h5-bug.png)

- Edit category
    - Dev tools highlighted the contrast in the edit category page these have been changed.
        - Dev tools image
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-dev.png)
        - Code before
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-code-before.png)
        - Code after
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-code-after.png)
        - Edit category after fix
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-after.png)

### Bugs highlighted during the development
 - Add movie button
 The add movie search button contrast needed adjusting so the text colour has been change from lounge blue lounge white.
    - Button before
        ### ![text](/documentation/development-bugs/add-movie-button/add-movie-before.png)
    - Code before
        ### ![text](/documentation/development-bugs/add-movie-button/search-movie-code-before.png)
    - Button after
        ### ![text](/documentation/development-bugs/add-movie-button/search-movie-after.png)
    - Code after
        ### ![text](/documentation/development-bugs/add-movie-button/search-code-after.png)
- Log inn button
The log in button mouse over was not displaying correctly so a lounge colour and bootstrap button class has been added.
    - Button before
        ### ![text](/documentation/development-bugs/log-in-button/login-button-before.png)
    - Button hover before
        ### ![text](/documentation/development-bugs/log-in-button/login-button-befor-mouse-over.png)
    - Code before
        ### ![text](/documentation/development-bugs/log-in-button/login-button-code-before.png)
    - Button after
        ### ![text](/documentation/development-bugs/log-in-button/login-button-after.png)
    - Code after
        ### ![text](/documentation/development-bugs/log-in-button/login-button-code-after.png)

- Category delete modal bug fix
The modal ids for button and modal needed a jinja id added for the category modal to work.
    - Code before
    ### ![text](/documentation/development-bugs/modal-bug/modal-bug-before.png)
    ### ![text](/documentation/development-bugs/modal-bug/modal-button-before.png)
    - Code after
    ### ![text](/documentation/development-bugs/modal-bug/modal-bug-before.png)
    ### ![text](/documentation/development-bugs/modal-bug/modal-button-after.png)

- Python error for add category build error.
During development with development set to on, errors are hinted when errors are made. In this case the rendered template did need to be changed to the correct template.
    - Error message
    ### ![text](/documentation/development-bugs/catgory-error/cat-build-error.png)
    - Code before
    ### ![text](/documentation/development-bugs/catgory-error/fixed-correct-url.png)
    - Code after
    ### ![text](/documentation/development-bugs/catgory-error/not-correct-ur.png)

- Movie href error for movie reset button.
During development with development set to on, errors are hinted when errors are made. In this case the movie reset button did not have correct jinja syntax.
    - Error message
    ### ![text](/documentation/development-bugs/movie-reset-button-error/reset-error.png)
    - Code before
    ### ![text](/documentation/development-bugs/movie-reset-button-error/reset-code-before.png)
    - Code after
    ### ![text](/documentation/development-bugs/movie-reset-button-error/reset-code-after.png)
***

## Further Testing

#### Browswers
-   The website has been tested on such browsers as: 
    -  Google Chrome 
    ### ![view](/documentation/broswer-and-device-images/desktop-crome.png)
    -  Microsoft Edge 
    ### ![view](/documentation/broswer-and-device-images/ms-edge.png)
    -  Firefox
    ### ![view](/documentation/broswer-and-device-images/firefox.png)
#### Devices
-   The website was viewed on such devices as: 
     - Desktop 
     ### ![view](/documentation/broswer-and-device-images/desktop-crome.png)
     - Laptop 
     ### ![view](/documentation/broswer-and-device-images/laptop.png)
     - Samsung Galaxy note 10 
     ### ![view](/documentation/broswer-and-device-images/note-10.jpg)
     - Samsung tablet 3 
     ### ![view](/documentation/broswer-and-device-images/note-3.png)
-   A large amount of testing was done to ensure that all pages were linking correctly.
***
### Defencive testing
Defencive programing has been used to stop users not logged in, or users that have not created messages answers or movies from adding, editing or deleteing them in the database. A flash message is displayed when access is denied.
- Question messages
    - Add message when a user is not logged in.
    ## ![text](/documentation/defencive-prog/logged-out-add-msg.png)
    - Edit message when a user is not logged in.
    ## ![text](/documentation/defencive-prog/logged-out-edit-msg.png)
    - Delete message when a user is not logged in.
    ## ![text](/documentation/defencive-prog/logged-out-del-msg.png)
    - Edit message when the user who created it is not logged in.
    ## ![text](/documentation/defencive-prog/non-user-edit-msg.png)
    - Delete message when the user who created it is is not logged in.
    ## ![text](/documentation/defencive-prog/non-user-del-msg.png)
- Answer/Reply messages
    - Add reply message when a user is not logged in.
    ## ![text](/documentation/defencive-prog/logged-out-add-reply.png)
    - Edit message when a user is not logged in.
    ## ![text](/documentation/defencive-prog/loged-out-edit-reply.png)
    - Delete message when a user is not logged in.
    ## ![text](/documentation/defencive-prog/logged-out-del-reply.png)
    - Edit message when the user who created it is not logged in.
    ## ![text](/documentation/defencive-prog/non-user-edit-reply.png)
    - Delete message when the user who created it is not logged in.
    ## ![text](/documentation/defencive-prog/non-user-del-reply.png)
- Movies
    - Add movie when a user is not logged in.
    ## ![text](/documentation/defencive-prog/logged-out-add-movie.png)
    - Edit movie when a user is not logged in.
    ## ![text](/documentation/defencive-prog/loged-out-edit-movie.png)
    - Delete movie when a user is not logged in.
    ## ![text](/documentation/defencive-prog/logged-out-del-movie.png)
    - Edit movie when the user who created is not loggged in.
    ## ![text](/documentation/defencive-prog/non-user-edit-movie.png)
    - Delete movie when the user who created is is not logged in.
    ## ![text](/documentation/defencive-prog/non-user-del-movie.png)
- Categories
    - Not admin logged in add category.
    ## ![text](/documentation/defencive-prog/add-cat.png)
    - Not admin logged in edit category.
    ## ![text](/documentation/defencive-prog/add-cat.png)
    - Not admin logged in delete category.
    ## ![text](/documentation/defencive-prog/add-cat.png)
***
### Testing error messages
- Error 404
### ![view](/documentation/error-pages/error-404.png)
- Error 500
### ![view](/documentation/error-pages/error-500.png)
***
### User Testing
-   The website has been tested by friends and family members to review the site and documentation to point out any bugs and/ or user experience issues.
    #### User testing bugs
    - The delete message modal was found to stiil say delete movie because it was copyied form the delete movie modal. This has to fixed with the correct Delete question message.
        - Bofore fix
        #### ![text](/documentation/user-bugs/del-q-before.png)
        - After fix
        #### ![text](/documentation/user-bugs/del-q-after.png)
    - The Edit Reply messsgae page title was found too still say Message Reply as it was copied ffrom the message reply passge and was fixed to say Edit Reply Message.
        - Before fix
        #### ![text](/documentation/user-bugs/edit-reply-before.png)
        - After fix
        #### ![text](/documentation/user-bugs/edit-reply-after.png)
    -  The edit message function for edit message method post was not update the new selected category_name in the movieloung routes.py python file, and has been fixed.
        - Code before fix
        #### ![text](/documentation/user-bugs/edit-msg-code.png)
        - Code after fix
        #### ![text](/documentation/user-bugs/edit-msg-code-after.png)

### Testing User Stories from User Experience (UX) section in README.md
***
## User stories
- ### First time user goals
    
    1. As a First time user, I want to easily navigate to register and then log in when first entering the website application.
        - As a first time user, I can easily navigate to register.
        #### ![text](/documentation/introactive-images/nav.png) 
        #### ![text](/documentation/introactive-images/register.png)
        - As a first time user, I can am redirected to the login in page once registered.
        #### ![text](/documentation/introactive-images/login.png)
    2. As a First Time User, I want to navigate the website easily and interact with the content.
        - As a firsst time user I can easily navigate the website on small and large screens.
        #### ![text](/documentation/introactive-images/nav.png) 
        #### ![text](/documentation/introactive-images/nav-small.png)
        #### ![text](/documentation/introactive-images/nav-small-open.png)  
    3. As a first time user I want to easily navigate to search for movies and add them to my list.
        - As a first time user I can easily navigate to search for movies.
        #### ![text](/documentation/introactive-images/movie-search.png)
        - Ass a first time user I can easily add movies to my list.
        #### ![text](/documentation/introactive-images/movie-results.png) 
        #### ![text](/documentation/introactive-images/movie-add.png)  
    4. As a first time user I want to easily navigate to the message board and add a message question or reply to a message.
        - As a first time user I can easily add a question in the message board.
        #### ![text](/documentation/introactive-images/add-msg.png)
        - As a first time user I can easlity add a reply to a question in the message board.
        #### ![text](/documentation/introactive-images/msg-reply-btn.png) 

- ### Returning user goals
    1. As a Returning User, I want to edit and delete my messages.
        - As a returning user I can edit my messages.
        #### ![text](/documentation/introactive-images/edit-msg-page.png)
        #### ![text](/documentation/introactive-images/edit-reply-msg.png)
        - As a returning user I can delete my messages.
        #### ![text](/documentation/introactive-images/add-edi-del-msg.png)
        #### ![text](/documentation/introactive-images/del-msg-modal.png) 
        #### ![text](/documentation/introactive-images/del-reply-modal.png)  

    2. As a Returning User, I want to edit and delete my movie list.
        - As a returning user I can edit my movies.
        #### ![text](/documentation/introactive-images/edit-movie.png)
        - As a returning user I can delete my movies.
        #### ![text](/documentation/introactive-images/movie-info-after.png)
        #### ![text](/documentation/introactive-images/del-movie-modal.png)
     
    3. As a Returning User, I want to see any new messages.
        - As a returning user i can see any new messages.
        #### ![text](/documentation/introactive-images/add-edi-del-msg.png)
    4. As a Returning User, I want to see if anyone has replied to my questions.
        - As a returning user I can see any new message replies.
        #### ![text](/documentation/introactive-images/msg-reply-open.png)

- ### Frequent user goals
    1. As a Frequent user, I want to easily reply to any messages or questions.
        - As a frequent user I can easily reply to any message.
        #### ![text](/documentation/introactive-images/msg-reply-open.png)
        - As a frequent user I can easily reply to any message questions.
        #### ![text](/documentation/introactive-images/add-edi-del-msg.png)

    2. As a Frequent user, I want to easily edit and delete my movie list.
        - As a frequent user I can easily edit my movies.
        #### ![text](/documentation/introactive-images/edit-movie.png)
        - As a frequent user I can easily delete my movies.
        #### ![text](/documentation/introactive-images/del-movie-modal.png)

    3. As a Frequent user, I want to easily edit or delete any messages or questions.
        - As a frequent user I can easily edit my messages.
        #### ![text](/documentation/introactive-images/msg-reply-open.png)
        - As a frequent user I can easily edit my message questions.
        #### ![text](/documentation/introactive-images/add-edi-del-msg.png)
        - As a frequent user I can easily delete my messages.
        #### ![text](/documentation/introactive-images/del-msg-modal.png) 
        - As a frequent user I can easily delete my message questions.
        #### ![text](/documentation/introactive-images/del-reply-modal.png)

- ### End of user goals
    1. As a End of User, I want to delete all my messages and questions.
        - As a end of user I can delete all my messages.
    2. As a End of User, I want to delete my movie list.
        - As a end of user I can delete all my movies.

- ### Admin user goals
    1. As an Admin User, I want access to add questions and edit and delete  all questions on the movie lounge message board.
        - As an admin user I have access to add questions.
        #### ![text](/documentation/introactive-images/add-msg.png)
        - As an admin user I have full access to edit all questions.
        - As an admin user I have full access to delete all questions
        #### ![text](/documentation/introactive-images/add-edi-del-msg.png)
        - As an admin user I have full access to edit all reply messages.
        - As an admin user I have full access to delete all reply messages.
        #### ![text](/documentation/introactive-images/msg-reply-open.png)
        
    2. As an Admin User, I want access to add movies and edit and delete all users movie lists.
        - As an admin user I have full access to add a movie.
        #### ![text](/documentation/introactive-images/movie-add.png)
        - As an admin user I have full access to edit all user and my movies.
        #### ![text](/documentation/introactive-images/edit-movie.png)
        - As an admin user I have full access to delete all user and my movies.
        #### ![text](/documentation/introactive-images/movie-info-after.png)
        #### ![text](/documentation/introactive-images/del-movie-modal.png)

    3. As an Admin User, I want access to add, edit and delete all categories and related questions, messages and movie lists.
        - As an admin user I have full access to add categorys.
        #### ![text](/documentation/introactive-images/add-cat.png)
        #### ![text](/documentation/introactive-images/add-a-cat.png)
        - As an admin user I have full access to edit all categorys and questions, messages and movie lists.
        #### ![text](/documentation/introactive-images/edit-cat.png)
        - As an admin user I have full access to delete all categorys and related questions, messages and movie lists.
        #### ![text](/documentation/introactive-images/add-cat.png)
        #### ![text](/documentation/introactive-images/del-cat.png)
