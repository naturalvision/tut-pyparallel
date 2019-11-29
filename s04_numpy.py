# In this example, we're showing a numpy function that already uses
# threads under the hood.  Thus, trying to speed it up using multiple
# threads (or processes) only results in slower execution, as threads
# will compete for CPU time.

from multiprocessing.pool import ThreadPool
from timeit import timeit

import numpy as np


np.random.seed(42)
data = [np.random.random((500, 1000)) for i in range(20)]


def time_stmts(stmts, number=1):
    for stmt in stmts:
        print("Running {!r}...".format(stmt), end='\t', flush=True)
        result = timeit(stmt, number=number, globals=globals())
        print('took {:.2f} seconds'.format(result))


time_stmts([
    '[np.linalg.svd(da) for da in data]',
    'ThreadPool(4).map(np.linalg.svd, data)',
    ])
