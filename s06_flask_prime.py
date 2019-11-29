from flask import Flask
from flask import request


app = Flask(__name__)


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


@app.route('/prime')
def prime():
    if is_prime(int(request.args['n'])):
        return "It's a prime number!"
    else:
        return "Not a prime number!"


if __name__ == '__main__':
    # YOUR CODE HERE: Experiment with handling each request in a new
    # process by using the `processes` argument:
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, app, threaded=True, processes=1)
