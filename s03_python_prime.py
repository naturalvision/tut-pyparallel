# In this example, we're running a costly, pure Python function in
# parallel.  We see that running this function in parallel using
# threads does *not* speed up total execution time, as the threads
# will complete for the GIL.  Running the function in parallel with
# processes will make it run faster.


import random
from multiprocessing.pool import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from timeit import timeit


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def time_stmts(stmts, number=1):
    for stmt in stmts:
        print("Running {!r}...".format(stmt), end='\t', flush=True)
        result = timeit(stmt, number=number, globals=globals())
        print('took {:.2f} seconds'.format(result))


random.seed(42)
numbers = [random.randint(1e5, 1e6) for i in range(2000)]


time_stmts([
    '[is_prime(nu) for nu in numbers]',
    'ThreadPool(2).map(is_prime, numbers)',
    'ProcessPool(2).map(is_prime, numbers)',
    ])
