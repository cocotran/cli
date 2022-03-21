from operator import truediv


class Process:
    def __init__(self, id, arrival_time, burst_time, priority) -> None:
        self.PID: int = id
        self.arrival_time: float = arrival_time
        self.burst_time: float = burst_time
        self.priority: int = priority
        self.time_slot: int = None
        self.remaining_time: float = burst_time
        self.first_run = True

    def __repr__(self):
        return f"Process ID:{self.PID}, Arrival: {self.arrival_time}, Burst: {self.burst_time}, Priority: {self.priority}"

    @property
    def response(self):
        return None if self.first_run is None else self.first_run - self.arrival_time

    @property
    def turnaround(self):
        return None if self.completion_time is None else self.completion_time - self.arrival_time

    @property
    def wait(self):
        return None if self.turnaround is None else self.turnaround - self.burst_time

    # def is_empty(self):
    #     return len(self.queue) == 0

    # #Inserting elemetns based on priority of execution
    # def insert(self, data):
    #     try:
    #         max = 0
    #         for i in range(len(self.queue)):
    #             if self.queue[i] > self.queue[max]:
    #                 max =i
    #         item = self.queue[max]
    #         self.queue.append(data)
    #         return item
    #     except  Exception as err:
    #         print(err)
    #         exit()

    # def decrement_time(self, clock):
    #     enter_time = clock.get_CPUTime()
    #     while clock.get_CPUTime() - enter_time <= self.quantum_time:
    #         pass
    #     self.remaining_time -= clock.get_CPUTime() - enter_time
    #     if self.remaining_time < 0.1:
    #         self.finish()
    #     self.has_CPU = False

    # def finish(self):
    #     print("---------------------------------------------------------------------------------")
    #     # print("(Time, ms: " + Scheduler.getElapsedtime() + ") " + "Process #" + self.ID + " *FINISHED*")
    #     # print("(Time, ms: " + Scheduler.getElapsedtime() + ") " + "Process #" + self.ID +" Waiting Time: " + self.waiting_time)
    #     print("---------------------------------------------------------------------------------")
    #     self.is_finished = True
    #     self.has_CPU = False
