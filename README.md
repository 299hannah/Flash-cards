# Collaborators
> - Mwangi Hannah Wambui

> - John Paul Otieno
> - Martin Mylles

## Description

Your baby brother is studying for a really big test in school. To help him remember he uses these tiny flash cards where he writes anything he thinks seems important. But he always seems to lose them or they get destroyed in some way.
You decide to help him.

### User story
- A user must be authenticated to see his flashcards.
- A user's flash card can contain a title with some notes.
- Flashcards should be organized according to subjects/courses.
- A user can delete or update a flash card he has created.
- A user should see when the flash card was created and when it was last updated

## Setup/Installation
On your terminal, clone the project.
    
    $ git clone https://github.com/299hannah/Flash-cards
    

Navigate into the cloned project.

    $ cd Flash-cards

Create a `.env` file.

    $ touch .env

Inside `.env`, add the following and fill the empty fields with the appropriate values:

```python
SECRET_KEY=
DEBUG=True
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost','.herokuapp.com','127.0.0.1'
DISABLE_COLLECTSTATIC=1
CLOUD_NAME= 
API_KEY=
API_SECRET=
```
The CLOUD_NAME, API_KEY, and the API_SECRET are from your account on [Cloudinary](https://cloudinary.com/).

Create the virtual environment and install the requirements from `requirements.txt`

    $ python3 -m venv env
    $ . env/bin/activate
    $ pip install -r requirements.txt


Perform a migration.

    $ python3 manage.py migrate


Start the server to run locally.

    $ python3 manage.py runserver

## Technologies Used
- Django
- Python 3.8.5
- Bootstrap 4
- Postgresql
- Cloudinary
