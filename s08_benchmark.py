from collections import Counter
from multiprocessing.pool import ThreadPool
from time import time

import click
import requests


def do_request(url, imagebytes):
    files = {'image': ('image.jpg', imagebytes)}
    response = requests.post(url, files=files)
    return {
        'elapsed': response.elapsed.total_seconds(),
        'status': response.status_code,
        'text': response.text,
        }


@click.command()
@click.argument('url')
@click.option('--requests', '-n', default=100)
@click.option('--concurrency', '-c', default=10)
@click.option('--image', default='cat.jpg')
def main(url, requests, concurrency, image):
    print("Sending {} requests with concurrency level {}...".format(
        requests, concurrency))

    imagebytes = open(image, 'rb').read()
    pool = ThreadPool(concurrency)
    t0 = time()
    results = pool.starmap(do_request, [(url, imagebytes)] * requests)
    total_time = time() - t0

    print("Time taken for tests:  {:.3f} seconds".format(total_time))
    print("Requests per second:   {:.2f} [#/sec] (mean)".format(
        requests / total_time))
    print("Complete requests:     {}".format(
        len([r for r in results if r['status'] == 200])))
    print("Failed requests:       {}".format(
        len([r for r in results if r['status'] != 200])))
    print("Response texts:        {}".format(
        repr(Counter([r['text'] for r in results]))[:200]))


if __name__ == '__main__':
    main()
