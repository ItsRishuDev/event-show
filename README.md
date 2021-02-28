Try on web using link 
https://event-show.herokuapp.com/

OR

Setup The first thing to do is to clone the repository:

$ git clone https://github.com/ItsRishuDev/event-show.git 
$ cd event-show

Install virtualenv

$ pip install virtualenv 
$ pip install virtualenvwrapper

Create a virtual environment to install dependencies in and activate it:

$ mkvirtualenv event-env 

activate virtual environment by 
$ workon event-env 

Then install the dependencies:

(event-env)$ pip install -r requirements.txt Note the (crud-env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(crud-env)$ python manage.py runserver And navigate to http://127.0.0.1:8000/.

Now you are able to use event-show on your local computer
