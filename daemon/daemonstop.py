def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', action='store_true')
    parser.add_argument('--stop', action='store_true')
    args = parser.parse_args()
    if args.start:
        start_daemon()
    elif args.stop:
        stop_daemon()

if __name__ == '__main__':
    main()
    
"""
The stop_daemon function is also interesting.
It does the following:
1. It reads the child process ID from a file.
2. It sends a SIGINT signal to the child process.
3. It deletes the file containing the child process ID.
"""

def stop_daemon():
    pid = read_pid()
    if pid:
        os.kill(pid, signal.SIGINT)
        os.remove(PID_FILE)