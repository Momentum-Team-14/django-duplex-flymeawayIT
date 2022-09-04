You can open this Momentum Flashcards project by creating a virtual environment in Python Django .

First download the Github.com/Momentum-Team-14/django-duplex-flymeawayIT repository to a dirctory of your choice.

Navigate to that directory in iTerm2 and run pip install pipenv if not already installed. if installed run pipenv install django

Create a superuser in django by running ‘python manage.py createsuperuser (or ./ (instead of python)(with no space between slash and manage.py)) .  
b. Enter your desired username. Username: (any name) 
c. Email address: (any email)@example.com. ...
d. Password: ********** (press Enter) Password (again): ********* (press Enter).  You will not see the password displayed at the prompt while you are typing.
 Superuser created successfully.

Now activate the virtual environment by running “pipenv shell”. In the virtual environment, evidenced by the Python version info to the right in the command line, above the prompt, and the directory name in the parenthesis to the right of the Python version; i.e. v3.10.6 (flash_cards3).  

Now run ‘./manage.py runserver’ to start the project server running 

Open a Chrome browser window and type in the url 127.0.0.1:8000 and press Enter to render the page.

Add /admin to the end of the url and press Enter to see if the django admin login page opens and login, if you are required to, with your original superuser login . 
  