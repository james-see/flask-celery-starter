# flask-celery-starter

Quick starter for getting Flask and celery up and running quickly.

## Quickstart

1. Make sure you have `pipenv` installed and simply run `pipenv install --dev` and then you can even run `pipenv run apprunner.py`
2. Copy over the `example.env` to `.env` like `cp example.env .env` from root of project. This is the redis connection info path that you can set if different than the default.

## Slowstart

1. Install all dependancies using either the `pip3 install -r requirements.txt` or `pipenv install --dev`
2. Run `flask run` in a terminal window
3. Run `celery worker -A task.app` in another terminal window

## Why

To learn and not forget the Celery spin-up and run paradigm for future self projects.
