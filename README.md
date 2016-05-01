*NB: This is the repository that hosted my first personal webpage. The code quality is not very good, since this is the project I used in order to learn web technologies.*

---

old-hakloevno
=======

Repo for hosting my Django-powered [website](https://hakloev.no).

# Setup #

Create a virtualenv called whatever, where ever you want (this one is called env):

```bash
$ virtualenv env
```

Activate the virtualenv with: 

```bash
$ source ./env/bin/activate
```

virtualenv can be closed with the command

```bash
$ deactivate
```

## gunicorn/supervisorctl #

Setup gunicorn, supervisorctl and nginx 

## Requirements/dependecies ##

```python
1. If not active, activate the virtualenv
* source ./env/bin/activate
2. Install dependencies
* pip install -r /path/to/requirements.txt
```

## Initialization ##

```bash
1. python manage.py syncdb
2. python manage.py migrate
```
