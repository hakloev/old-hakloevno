hakloevno
=======

Repo for hosting my Django-powered [website](https://hakloev.no).

# Setup #

Create a virtualenv called whatever, where ever you want (this one is called env):

'''
$ virtualenv env
'''

Activate the virtualenv with: 

'''
$ source ./env/bin/activate
'''

virtualenv can be closed with the command

'''
$ deactivate
'''

## gunicorn/supervisorctl #

Setup gunicorn, supervisorctl and nginx 

## Requirements/dependecies ##

1. If not active, activate the virtualenv
* source ./env/bin/activate
2. Install dependencies
* pip install -r /path/to/requirements.txt

## Initialization ##

1. python manage.py syncdb
2. python manage.py migrate
