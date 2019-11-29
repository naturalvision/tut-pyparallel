# A slightly more interesting example.  Instead of sleeping, our
# parallelized function calls will now retrieve webpages.  The effect
# is the same, since we're doing IO that doesn't block the
# interpreter, though the numbers more noisy.

from multiprocessing.pool import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from pprint import pprint
from timeit import timeit

import requests


def time_stmts(stmts, number=1):
    for stmt in stmts:
        print("Running {!r}...".format(stmt), end='\t', flush=True)
        result = timeit(stmt, number=number, globals=globals())
        print('took {:.2f} seconds'.format(result))


urls = [
    'https://www.google.com',
    'https://duckduckgo.com',
    'https://en.wikipedia.org',
    'http://pythong.org/',
    'http://pythong.org/morehoff.html',
    ]


pprint([(url, requests.get(url).elapsed.total_seconds()) for url in urls])
print()


time_stmts([
    '[requests.get(url) for url in urls]',
    'ThreadPool(4).map(requests.get, urls)',
    'ProcessPool(4).map(requests.get, urls)',
    ], number=2)
