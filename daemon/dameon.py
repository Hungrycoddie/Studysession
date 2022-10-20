return read_config(base_dir / 'config.yaml')

def main():
    config = read_config(base_dir / 'config.yaml')
    config_logging(config)

    if len(sys.argv) > 1:
        if sys.argv[1] == 'start':
            command = config['command']
            log_file_path = base_dir / 'daemon.log'
            create_daemon(command, log_file_path)
        elif sys.argv[1] == 'stop':
            pid_file = base_dir / 'daemon.pid'
            if not pid_file.exists():
                raise Exception('Daemon is not running')

            with pid_file.open() as file:
                pid = int(file.read())
            os.kill(pid, signal.SIGINT)
            pid_file.unlink()
        else:
            raise Exception('Unknown command')
    else:
        print('Usage: {} start|stop'.format(sys.argv[0]))



if __name__ == '__main__':
    main()