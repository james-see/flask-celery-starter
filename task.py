import celery
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = celery.Celery('celery-sample')
app.conf.broker_url = os.getenv('REDIS_CONNECT')
app.conf.result_backend = os.getenv('REDIS_CONNECT')

@app.task
def hello(name):
    return "Hello "+name

