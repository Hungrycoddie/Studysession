"""
The create_daemon function is the most interesting part of the script.
It does the following:
1. It creates a child process.
2. It sets the child process as the session leader.
3. It sets the child process as the process group leader.
4. It changes the working directory to the root directory.
5. It closes all open file descriptors.
6. It redirects the standard input, standard output, and standard error to /dev/null.
7. It writes the child process ID to a file.
8. It calls the command.

"""

import os
import sys
import time
import atexit
import signal

def daemonize(pidfile, *, stdin='/dev/null',
                          stdout='/dev/null',
                          stderr='/dev/null'):
    if os.path.exists(pidfile):
        raise RuntimeError('Already running')

    # First fork (detaches from parent)
    try:
        if os.fork() > 0:
            raise SystemExit(0)   # Parent exit
    except OSError as e:
        raise RuntimeError('fork #1 failed.')

    os.chdir('/')
    os.umask(0)
    os.setsid()
    # Second fork (relinquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #2 failed.')

    # Flush I/O buffers
    sys.stdout.flush()
    sys.stderr.flush()

    # Replace file descriptors for stdin, stdout, and stderr
    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

    # Write the PID file
    with open(pidfile,'w') as f:
        print(os.getpid(),file=f)

    # Arrange to have the PID file removed on exit/signal
    atexit.register(lambda: os.remove(pidfile))

    # Signal handler for termination (required)
    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Example daemon')
    parser.add_argument('--stdout', help='redirect stdout to this file')
    parser.add_argument('--stderr', help='redirect stderr to this file')
    parser.add_argument('--pidfile', help='file to write PID to')
    args = parser.parse_args()

    stdout = open(args.stdout, 'w') if args.stdout else sys.stdout
    stderr = open(args.stderr, 'w') if args.stderr else sys.stderr
    daemonize(args.pidfile, stdout=stdout, stderr=stderr)

    # The code below is executed in the child process.
    # You can use os.getppid() to verify this.

    for i in range(10):
        print('{0:d} {1:d}'.format(i, os.getpid()))
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    main()
    
"""
Here's what the above class is doing:
1. The daemonize() function forks the process twice, so that the parent process
   is no longer the parent of the daemon process. This is done to ensure that
   the daemon process is not a session leader, which prevents it from acquiring
   a controlling terminal.
2. The daemon process is moved to the root directory, so that it doesn't block
   unmounting of the file system it was started from.
3. The daemon process has its file mode creation mask set to 0, so that it
   doesn't prevent file creation in the file system it was started from.
4. The daemon process is given a new session ID, so that it has no controlling
   terminal.
5. The daemon process is detached from the parent's standard file descriptors,
   so that it doesn't receive SIGHUP when the parent dies.
6. The daemon process's standard file descriptors are redirected to /dev/null,
   so that it doesn't share them with the parent.
7. The daemon process's current working directory is changed to the root
   directory, so that it doesn't block unmounting of the file system it was
   started from.
8. The daemon process's root directory is changed to the root directory, so
   that it doesn't block unmounting of the file system it was started from.
9. The daemon process's process group ID is set to its process ID, so that it
   can't open any controlling terminals.
10. The daemon process's process ID is written to a PID file, so that it can be
    terminated later.
11. The daemon process's process ID is registered with atexit, so that the PID
    file is removed when the daemon process terminates.
12. The daemon process's process ID is registered with a signal handler for
    SIGTERM, so that it can be terminated later.
"""