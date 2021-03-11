# Assignment 11

## Objective
Add an SQLite database file to the django project and create a history table

1. Django comes with a bunch of pre-installe apps (such as admin) we need to migrate the database to create the tables for these apps. This is kind of a cleanup we need to do since django has unapplied migrations by default. Run `python manage.py migrate` to migrate the migrations. You can think of migrations as atomic changes we want to make to our database. Every time you make a change to your `models.py` file you will need to run `python manage.py makemigrations` - this will create a migration file which defines the changes you want to make to the database. Over time you will create a large folder of changes you made to your database over the course of development. This folder of your database schema history will come in handy when you want to create a new database with your specifications. Or, imagine there is a database which you startup up a month ago, you can run `python manage.py migrate` and django will know exaclty how to bring that database up to speed based off your migrations folder. In summary, this is the flow of working with databases using a modern web framework like Django.

    1. python manage.py makemigrations
    2. python manage.py migrate

2. Create a new file in your Django app folder called `models.py`.
3. Type `from django.db import models` at the top of your models folder.
4. Use the models folder (and some Django guides) to create a new database table called `CalculateHistory`. HINT: your models.py file should contain a line similar to `class CalculateHistory(models.Model)`.
5. Add two columns to your new class/table: `input` and `result`. They should both be `CharFields` with `max_length=100`.
6. Save the models.py file.
7. Add your django app to the list of `INSTALLED_APPS` in your `settings.py` file.
8. Run `python manage.py makemigrations <YOUR_DJANGO_APP>`.
9. Run `python manage.py migrate`.
10. The two previous commands will create a migrations file containing your new table and then apply that migration to an SQLite database. SQLite is a minimal database which simply lives on your computer as a file, other databases exist as an entire program that runs in the background.
10. When you run python manage.py migrate django will create a new SQLite file for you since it doesn't exist yet.

## POGGGERS CHECKPOINT - we will now put our history into our newly created table

11. At the top of your views file import your model. `from <YOUR_DJANGO_APP>.models import CalculateHistory`. We can interact with your new model the same way we interact with any other class. Since your new models *inhertited* from the models.Model Django class it will expose lots of helpful features for interacting with the database.
12. Some where in your calculate view we will need to save the history to our database table. To make a new database row write
```
row = CalculateHistory(input=<YOUR_INPUT>, output=<YOUR_OUTPUT>)
row.save()
```
13. Run your view to save a row to your database.
14. BOOM we saved an entry to our database. Now use one of the two methods below to inspect the contents of your database.

## Resources
* [Writing your first Django app, part 2](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)
* There are multiple ways to see the contents of your database. A couple convenient ways given by Django are to use the [Django shell](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api) and the [Django admin console](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-an-admin-user).