# Task_tracker

## Description
The project allows you to maintain a database of company tasks, track deadlines and stages of their implementation, and distribute them among employees in the most rational way.

## Requirements
- `Python`
- `PostgreSQL`

## Prepare
- Create a `.env` configuration file with your personal settings in the root of the project, according to the sample, specified in `.env.sample`. Fill out the file according to your personal data;
- Create a database in postgresql. The name of the database must match the name specified in the file;
- Migrate your database using command: `python manage.py migrate`;

## Running
To run the project, enter the `python manage.py runserver` command in the terminal.
<br>The project is ready to use!

## Docker
If you want to use Docker enter the following commands in the terminal:
- build the image with the command: `docker-compose build`;
- run the container with the command: `docker-compose up`.

## Work with API (documentation)
Use the following links to read the documentation. It describes the details of working with the project API.
- http://127.0.0.1:8000/docs/ - user registration
- http://127.0.0.1:8000/redoc/ - show all users
