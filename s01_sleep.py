# Demonstrate use of 'ThreadPool' and 'ProcessPool' to parallelize
# function calls across threads and processes respectively.

# 'time.sleep' can be parallelized within Python threads because it
# does not lock the GIL.

from multiprocessing.pool import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from time import sleep
from timeit import timeit


def time_stmts(stmts, number=1):
    for stmt in stmts:
        print("Running {!r}...".format(stmt), end='\t', flush=True)
        result = timeit(stmt, number=number, globals=globals())
        print('took {:.2f} seconds'.format(result))


time_stmts([
    '[sleep(i) for i in range(4)]',
    'ThreadPool(4).map(sleep, range(4))',
    'ProcessPool(4).map(sleep, range(4))',
    ])
