from time import sleep
from process import Process
from clock import Clock


class Scheduler:

    def __init__(self, processes) -> None:
        self.all_processes = iter(processes)
        self.active_queue = [process for process in processes if process.arrival_time <= 1000]
        self.expired_queue = []

        self.wall_clock = 0
        self.running = None  # Running process
        self.run_start = None  # Time the running process started running
        self.next_submit = self.get_next_submit()

    def get_time_slot(self, priority: int) -> int:
        """Returns the time slot in millisecond"""
        return (140 - priority) * (20 if priority < 100 else 5)

    def get_updated_priority() -> int:
        pass

    def add_to_expired_queue(self, new_process: Process) -> None:
        # Get the index
        low = 0
        high = len(self.expired_queue)
        while low < high:
            mid: int = (low + high) >> 1
            if self.expired_queue[mid].priority < new_process.priority:
                low = mid + 1
            else:
                high = mid
        self.expired_queue.insert(low, new_process)

    def switch_flag(self) -> None:
        if len(self.active_queue) > 0:
            return
        self.active_queue = self.expired_queue
        self.expired_queue = []

    def schedule_execution(self):
        for process in self.active_queue:
            if process.time_slot is None:
                process.time_slot = self.get_time_slot(process.priority)

    def update_priority(self, process: Process):
        # process.waiting_time =
        # bonus =
        pass

    def get_next_submit(self):
        return next(self.all_processes, None)

    def run(self, process: Process):
        # ------------- Start --------------
        self.running = process
        if self.running is None:
            self.run_start = None
            return
        if self.running.first_run:
            self.running.first_run = False
            print(f"Time {self.wall_clock}, {self.running.PID}, Started, Granted {self.running.time_slot}")
        else:
            print(f"Time {self.wall_clock}, {self.running.PID}, Resumed, Granted {self.running.time_slot}")
        self.run_start = self.wall_clock

    def start(self):
        while True:
            if len(self.active_queue) == 0 and len(self.expired_queue) == 0:
                print("Exit")
                return

            self.switch_flag()
            print(self.active_queue)

            fast_forward_time = 0

            # Handle completion first
            # if self.running and (self.next_submit is None or self.run_start + self.running.remaining_time <= self.next_submit.arrival_time):
            if self.running:
                print(f"Time {self.wall_clock}, {self.running.PID}, Terminated")
                self.wall_clock = self.run_start + self.running.time_slot
                self.running.remaining_time = self.running.burst_time - self.running.time_slot
                self.add_to_expired_queue(self.active_queue.pop(0))
                self.run(self.active_queue[0] if self.active_queue else None)
                fast_forward_time = self.running.time_slot
                continue

            # Handle a new arrival, if there is one
            # if self.all_processes and (self.running is None or self.next_submit.arrival_time < self.running.remaining_time):
            if self.all_processes and (self.next_submit.arrival_time < fast_forward_time):
                print(f'Time {self.next_submit.arrival_time}, {self.next_submit.PID}, Arrived')
                self.add_to_expired_queue(self.next_submit)
                
                # new_process = self.next_submit
                # self.wall_clock = new_process.arrival_time
                # new_time_remaining = new_process.remaining_time
                # if self.running:
                #     running_time_remaining = self.running.remaining_time - (self.wall_clock - self.run_start)
                #     if new_time_remaining < running_time_remaining:
                #         print(f"Time {self.wall_clock}, {self.running.PID}, Paused")
                #         self.running.remaining_time = running_time_remaining
                #         self.run(new_process)
                #     self.waiting.append(self.running)
                # else:
                #     self.run(new_process)
                self.next_submit = self.get_next_submit()

            self.wall_clock += fast_forward_time
            sleep(1)