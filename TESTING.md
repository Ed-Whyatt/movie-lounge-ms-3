# Testing

## pep8
***
## W3C Markup Validator [link](https://validator.w3.org/#validate_by_uri)
***
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
All pages have been checked with the base page active for meta data to be loaded for errors.
- Base html used for main nvagation and footer on all pages base.html.
### ![text](/documentation/w3-validator/base.png)
- Add category page add_category.html
### ![text](/documentation/w3-validator/add-cat.png)
- Add movie search page add_movie.html
### ![text](/documentation/w3-validator/add-movie.png)
- Add a question for the message booard questions add_questuion.html
### ![text](/documentation/w3-validator/add-question.png)
- Add a reply to the question on the message borad add_reply.html
### ![text](/documentation/w3-validator/add-reply.png)
- Categorys view categories.html
### ![text](/documentation/w3-validator/categories.png)
- Edit categorys edit_category.html
### ![text](/documentation/w3-validator/edit-cat.png)
- Edit movie page edit_movie.html
### ![text](/documentation/w3-validator/edit-movie.png)
- Edit question page edit_question.html
### ![text](/documentation/w3-validator/edit-question.png)
- Edit reply edit_reply.html
### ![text](/documentation/w3-validator/edit-reply.png)
- Login page login.html
### ![text](/documentation/w3-validator/login.png)
- Message borad displays the message questions and replys message_board.html
### ![text](/documentation/w3-validator/message-board.png)
- Movie pahe witch is the home page displaying users movies movie.html
### ![text](/documentation/w3-validator/movie.jpg)
- Register page register.html
### ![text](/documentation/w3-validator/register.png)
- Search results that displays the add movie seach results search_results.html
### ![text](/documentation/w3-validator/search-results.png)
- Selected movie that displays the selected movie for a user to add to there list select_movie.html
### ![text](/documentation/w3-validator/select-movie.png)

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
## Google dev tool lighhouse hilighted bugs.
- Home page
    - Dev tools hilighted modal aria ids and element order witch have been fixed by adding loop-index to modal ids and aria attributes.
    ### ![text](/documentation/dev-lighthouse/home-page-lh/home-lh-aria-bug.png)
    ### ![text](/documentation/dev-lighthouse/home-page-lh/heme-page-h5-bug.png)

- Edit category
    - Dev tools hilighted the contrast in the edit category page these have been changed.
        - Dev tools image
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-dev.png)
        - Code before
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-code-before.png)
        - Code after
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-code-after.png)
        - Edit category after fix
        ### ![text](/documentation/dev-lighthouse/edit-categorg-lh/edit-cat-after.png)

### Bugs hilighted during the development
 - Add movie button
 The add movie search button contrast needed ajusting so the text color has been change from lounge blue lounge white.
    - Button before
        ### ![text](/documentation/development-bugs/add-movie-button/add-movie-before.png)
    - Code before
        ### ![text](/documentation/development-bugs/add-movie-button/search-movie-code-before.png)
    - Button after
        ### ![text](/documentation/development-bugs/add-movie-button/search-movie-after.png)
    - Code after
        ### ![text](/documentation/development-bugs/add-movie-button/search-code-after.png)
- Log inn button
The log in button mouse over was not displaying correctly so a lounge colour and bootstap button class has been added.
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
 ### Further Testing

-   The website has been tested on such browsers as: 
    -  Google Chrome [view](documentation/broswer-and-device-images/desktop-crome.png)
    -  Microsoft Edge [view](documentation/broswer-and-device-images/ms-edge.png)
    -  Firefox [view](documentation/broswer-and-device-images/firefox.png)
-   The website was viewed on such devices as: 
     - Desktop [view](documentation/broswer-and-device-images/desktop-crome.png)
     - Laptop [view](/documentation/broswer-and-device-images/laptop.png)
     - Samsung Galaxy note 10 [view](documentation/broswer-and-device-images/note-10.jpg)
     - Samsung tablet 3 [view](documentation/broswer-and-device-images/note-3.png)
-   A large amount of testing was done to ensure that all pages were linking correctly.

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

### User stories
***

