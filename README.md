# Training-Concepts


### Running the project

* locally  
``python runserver.py runserver``


### Database migrations
* initialize
``python runserver.py db init``

* generate migrations from the database
``python runserver.py db migrate``

* apply migrations to the database
``python runserver.py db upgrade``
