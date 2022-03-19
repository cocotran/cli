from process import Process
from clock import Clock


class Scheduler:
    def __init__(self, processes) -> None:
        self.active_queue = [process for process in processes if process.arrival_time <= 1000]
        self.expired_queue = [process for process in processes if process.arrival_time > 1000]

    def run(self, clock: Clock):
        # ------------- Start --------------
        first_process = self.active_queue[0]
        first_process.time_slot = self.get_time_slot(first_process.priority)
        print(f"Time 1000, {first_process.PID}, Started, Granted {first_process.time_slot}")

        clock.fast_forward(first_process.time_slot)

    def get_time_slot(self, priority: int) -> int:
        """Returns the time slot in millisecond"""
        return (140 - priority) * (20 if priority < 100 else 5)

    def get_updated_priority() -> int:
        pass

    def accept_new_process(self, new_process: Process) -> None:
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
