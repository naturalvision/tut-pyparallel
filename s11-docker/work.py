from datetime import datetime
import sys
from time import sleep


def work(output_fn, seconds):
    with open(output_fn, 'a') as f:
        for i in range(seconds):
            now = datetime.now().isoformat()
            print(now)
            print(now, file=f, flush=True)
            sleep(1)


if __name__ == '__main__':
    work(sys.argv[1], int(sys.argv[2]))
