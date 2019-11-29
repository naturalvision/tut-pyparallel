import os
import subprocess
import sys


def run(args):
    process = subprocess.Popen(
        args=args,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        close_fds=True,
        )
    print("Running", args)
    print("- my PID:          ", os.getpid())
    print("- subprocess PID:  ", process.pid)
    process.wait()


def spawn_daemon(function, *args, **kwargs):
    # First fork
    pid = os.fork()
    if pid != 0:  # parent returns
        os.waitid(os.P_PID, pid, os.WEXITED)
        return

    # Decouple from parent environment
    # os.chdir("/")
    os.setsid()
    os.umask(0)

    # Do second fork
    pid = os.fork()
    if pid != 0:  # parent exits
        os._exit(0)

    function(*args, **kwargs)


def main(argv=sys.argv[1:]):
    if hasattr(os, 'fork'):
        spawn_daemon(run, argv)
    else:
        run(argv)


if __name__ == '__main__':
    main()
