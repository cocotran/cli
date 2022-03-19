from time import sleep


class Clock:
    def __init__(self, step=1, cycles=0, stop=False):
        self.current_time = 0
        self.step = step
        self.cpu_cycles = cycles
        self.stop = True

    def set_timer(self, count):
        self.count = count

    def get_current_time(self):
        return self.current_time

    def get_CPUCycles(self):
        return self.cpu_cycles

    def start_clock(self):
        if self.stop:
            self.stop = False
        while not self.stop:
            self.current_time += self.step
            sleep(1)

    def stop_clock(self):
        self.stop = True

    def fast_forward(self, time):
        self.current_time += time