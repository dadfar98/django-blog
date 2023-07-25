# An Itelli fund Blog engine build with django.

## Development:
1. Clone Repository:

        git clone https://bitbucket.org/mykolbeh/blog.git
        cd blog

2. For latest code changes (optional):

         git pull origin develop
         git checkout develop

3. Create a virtual environment (strongly advised):

   if virtualenv is not installed:

        pip install virtualenv

   create a virtual environment called venv

       virtualenv venv

   activate the environment:

   On Linux:

       source venv/bin/activate

   On windows:

       venv\Scripts\activate

   deactivate environment:

       deactivate

4. Install dependencies in virtual environment:

        pip install -r requirements.txt

5. Create .env file:
 
        cp .env.example .env

    **change the "SECRET_KEY"**
    
    if you plan to use a sqlite db, you're good to go. 

    if you use postgres, first you should create a new database.

    then provide the database connection specifics in .env file.

6. Migrate:
    
        python manage.py migrate

7. Run development server:
    
    using the default port 8000

        python manage.py runserver

    using custom provided port eg: 12000

        python manage.py runserver 0.0.0.0:12000
        