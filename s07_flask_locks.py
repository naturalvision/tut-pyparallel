from multiprocessing import Lock
from random import choice
from time import sleep

from flask import Flask
from flask import request


app = Flask(__name__)


def do_io_stuff(s=0.01):
    sleep(s)
    return choice([True, False])


def do_cpu_stuff(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def model_true(): return sleep(0.01) or 1
def model_false(): return sleep(0.01) or 0
model_true_lock = Lock()
model_false_lock = Lock()


@app.route('/predict')
def predict():
    do_cpu_stuff(int(request.args['n']))
    if do_io_stuff():
        with model_true_lock:
            prediction = model_true()
    else:
        with model_false_lock:
            prediction = model_false()
    return "The answer is {}".format(prediction)
