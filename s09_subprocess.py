import os
import subprocess
import sys


process = subprocess.Popen(
    args=sys.argv[1:],
    stdin=subprocess.DEVNULL,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    close_fds=True,
    )
print("My PID:               ", os.getpid())
print("Spawned process PID:  ", process.pid)
input("Press any key to exit {}\n".format(sys.argv[0]))
