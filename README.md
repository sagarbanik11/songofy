#    Songofy Music Django Web App
###    This is a web application built using python django framework. This app uses django version 3.0.4 in the backend and postgres sql at the database side. This app has a basic front end developed using bootstrap css and js. This application is built and tested for python version 3.8.

Installation Steps
==================

1.  Install python 3.8 if not done already.
2.  Download and extract application.
3.  Import the project to an IDE of your choice.
4.  Configure your database details in settings.py file.
![landing page](https://bitbucket.org/sagarbanik/songofy/raw/97bc96417666072be91bc78d56c8af7b9343dca7/media/readme/database.png)
4.  Database file SongofyDB is in root directory.
5.  Execute following commands to setup your database with necessary tables.
```
        python manage.py makemigrations
        python manage.py migrate
```
6.  Now run the application.
```
        python manage.py runserver
```
6.   Browse through the app and Happy coding.

Screenshots
==================

###    Landing Page

![landing page](https://bitbucket.org/sagarbanik/songofy/raw/97bc96417666072be91bc78d56c8af7b9343dca7/media/readme/landingpage.png)

###    User Login

![loginpage](https://bitbucket.org/sagarbanik/songofy/raw/97bc96417666072be91bc78d56c8af7b9343dca7/media/readme/login.png)

###    User Registraion

![Reg_page](https://bitbucket.org/sagarbanik/songofy/raw/97bc96417666072be91bc78d56c8af7b9343dca7/media/readme/registraion.png)

###    Add Song

![Add Song](https://bitbucket.org/sagarbanik/songofy/raw/97bc96417666072be91bc78d56c8af7b9343dca7/media/readme/addsong.png)

###    Add New Artist with Ajax

![Add Artist](https://bitbucket.org/sagarbanik/songofy/raw/97bc96417666072be91bc78d56c8af7b9343dca7/media/readme/addartist.png)

###    Website: https://songofy.herokuapp.com
