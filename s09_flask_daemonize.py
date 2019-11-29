from time import sleep

from flask import Flask
from flask import request

import s09_daemonize


app = Flask(__name__)


@app.route('/run')
def run():
    args = request.args['command'].split()
    s09_daemonize.main(args)
    return "I think I spawned something!"


def this(output_fn):
    with open(output_fn, 'a') as f:
        for i in range(10):
            print(i, file=f, flush=True)
            sleep(1)


@app.route('/runthis')
def runthis():
    output_fn = request.args['output']
    s09_daemonize.spawn_daemon(this, output_fn)
    return "I did this!"


app.run()
