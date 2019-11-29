import time

from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/sleep')
def sleep():
    seconds = float(request.args.get('seconds', '1'))
    time.sleep(seconds)
    return 'Done sleeping!'


if __name__ == '__main__':
    # YOUR CODE HERE: Experiment with handling each request in a new
    # process by using the `processes` argument:
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, app, threaded=True, processes=1)
