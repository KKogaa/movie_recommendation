# Movie recommendation system

Movie recommendation system based on Giya REST boilerplate that uses Flask-RESTX (formerly Flask-RESTPlus).

# Features

* Full featured framework for fast, easy, and documented API with [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
* JSON Web Token Authentication with [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
* Swagger Documentation (Part of Flask-RESTX).
* Unit Testing.
* Database ORM with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* Database Migrations using [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)
* Object serialization/deserialization with [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* Data validations with Marshmallow [Marshmallow](https://marshmallow.readthedocs.io/en/stable/quickstart.html#validation)

## Flask CLI help command output:
```sh
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a
  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
  will enable debug mode.

    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  db      Perform database migrations.
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
  test    Run unit tests
```


## Packages
```sh
python3 -m venv env
pip3 install -r requirements.txt
```


## Running
Please specify your app's environment variables in a `.env` file, otherwise Flask CLI wouldn't find your app.

```sh
# .env file example
export FLASK_APP=giya

# configs: production, testing, development, and default (uses DevelopmentConfig)
export FLASK_CONFIG=development

# Another way of assigning environment variables is:
FLASK_APP=giya
FLASK_CONFIG=development

# Read more at https://github.com/theskumar/python-dotenv
```

```sh
# Enter the virtualenv
$ source env/bin/activate

# (Optional for development, recommended)
$ flask db init # Initializes a new SQLite database.
$ flask db migrate # Creates the tables in the database.

# update database
$ flask db migrate
$ flask db upgrade

# Run the app
$ flask run
```



## Unit testing
Giya has already some unit tests written, we encourage adding more unit tests as you scale.

```sh
# Unit testing
$ flask test

# Run specific unit test(s)
$ flask test tests.test_auth_api tests.test_user_model ...
```
