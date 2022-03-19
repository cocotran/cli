from concurrent.futures import process
from re import T
import sys
from time import sleep

from utils import read_input
from process import Process
from clock import Clock
from scheduler import Scheduler

global processes
processes = []

def main(args):
    processes_settings = read_input(args[1])
    for i in range(1, len(processes_settings)):
        settings = processes_settings[i].strip().split(" ")
        processes.append(Process(
            settings[0], int(settings[1]), int(settings[2]), int(settings[3])
        ))

    scheduler = Scheduler(processes)
    scheduler.run()

if __name__ == "__main__":
    main(sys.argv)
