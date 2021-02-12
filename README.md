# Dockerized Flask WebApp on Azure

This project is built from [Flask React Quickstart](https://github.com/qubitron/flask-webapp-quickstart)

Authentication and structure was infulenced by [Handle User Accounts & Authentication in Flask with Flask-Login](https://hackersandslackers.com/flask-login-user-authentication/)

## [Deployed on Azure](http://homework1webapp.azurewebsites.net/)

To get started, install python 3.7+ if not already installed. Then initialize a virtual python environment and activate it:

```bash
$ py -3 -m venv env
$ env\scripts\activate
```

Next, install required dependencies:

```bash
$ pip install -r requirements.txt
```

Then you can simply run the webapp locally with:

```bash
py server/src/app.py
```

The app can also be run locally in docker with:

```bash
docker-compose up
```