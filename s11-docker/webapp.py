import os

from flask import escape
from flask import Flask
from flask import request
from redis import Redis
from rq.job import Job
from rq import Queue


from work import work


app = Flask(__name__)

redis_connection = Redis(
    host=os.environ['REDIS_HOST'],
    port=int(os.environ['REDIS_PORT']),
    )
task_queue = Queue('my-queue', connection=redis_connection)


@app.route('/run')
def run():
    output_fn = request.args['output']
    seconds = int(request.args.get('seconds', '10'))
    job = task_queue.enqueue(work, output_fn, seconds)
    return "Enqueued job with id {}".format(job.id)


@app.route('/status/<job_id>')
def status(job_id):
    job = Job.fetch(job_id, connection=redis_connection)
    return escape("{} {}".format(job, job.get_status()))


if __name__ == '__main__':
    app.run()
