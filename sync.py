from dirsync import sync
import logging
import threading
import os
import argparse

class FileLogger:
    def __init__(self, log_path):
        logfile = os.path.join(log_path, 'sync.log')
        logging.basicConfig(filename=logfile, format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    def info(self, record):
        print(record)
        logging.info(record)

def sync_folders(source_path, target_path, interval, log_path):
    threading.Timer(interval, sync_folders, [source_path, target_path, interval, log_path]).start()
    sync(source_path, target_path, "sync",  create=True, purge=True, logger=FileLogger(log_path))

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_path", type=str, help="Source folder path")
    parser.add_argument("target_path", type=str, help="Target folder path")
    parser.add_argument("interval", type=float, help="Interval")
    parser.add_argument("log_path", type=str, help="Log file path")
    args = parser.parse_args()
    return args

def main():
    args = get_arguments()
    sync_folders(args.source_path, args.target_path, args.interval, args.log_path)

if __name__ == "__main__":
    main()
