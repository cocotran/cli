from math import e
import threading, os
from threading import Lock
from collections import deque 


class processInfo():
     def __init__(self, pid: str, burst_time: int, priority: int, arrival_time: int, processing_time: int):
        self.pid = pid
        """Process id """
        self.burst_time = burst_time
        
        self.priority = priority

        self.arrival_time = arrival_time
        """Arrival time to the ready queue"""
        self.remaining_time = processing_time
        """Time required before the process finishes"""

class process():

     def __init__(self, process_info: processInfo):
        self.process_info = process_info
        
        self.mutex = threading.Lock()             #To make sure only one process will get the CPU
        self.__arrivalTime = 1000
        self.__waiting_time = 0
        self.__hasCpu = False          #Pause or resume
        self.__isFinished = False
        self.__time_processed = 0

     def run(self):
         enterTime = os.currentTimeMillis()
         while( is_finished is not False):
           self.mutex.acquire()
                try:

                   if(self.hasCpu):
                     delta = os.currentTimeMillis()- enterTime
                     print(f"Time 1000, {first_process.PID}, Resumed, Granted {first_process.time_slot}")
                     #updateQuantum
                     #decrementTime
                     print(f"Time 1000, {first_process.PID}, Finished, Granted {first_process.time_slot}")

                    enterTime = os.currentTimeMillis()

                finally:
                  
                  self.mutex.release()


             

        
     def pid(self):
        """
        Returns the process ID
        """
        return self.process_info.pid

     def arrival_time(self):
        """
        Returns the arrival time
        """
        return self.process_info.arrival_time

     def burst_time(self):
        """
        Returns the burst time
        """
        return self.process_info.burst_time

     def priority(self):
        """
        Returns the priority
        """
        return self.process_info.priority
    
     def is_finished(self):
        """
        Returns if a process is finished 
        """
        return self.process_info.remaining_time <= self.__isFinished


     def timeSlice(self, allocated_time: int):
        """
        Executes the process for a given amount of time, each process runs for 1 time period
        """
        self.__on_executing(allocated_time)
        extra_time = 0
        if self.process_Info.remaining_time < allocated_time:
            # If we have more time to execute than is required then we need to account for that
            extra_time = allocated_time - self.remaining_time
            self.__time_processed = self.total_time_to_process
        else:
            self.__time_processed += allocated_time
        self.__on_executed(allocated_time, allocated_time - extra_time)
        if self.is_finished:
            self.__on_finished()
        return extra_time

     def time_processed(self):
        """
         Total time of a process during an excecution
        """
        return self.__time_processed

    
     def waiting_time(self):
        """
         The amount of time that the process has waited for without being executed.
        """
        return self.__waiting_time


     def remaining_time(self):
        """
       Remaining time before the process finishes executing.
        """
        return self.process_info.remaining_time - self.time_processed

     def has_CPU(self):
         """
         Indicates if the process has the CPU
         """
         return self.__hasCpu

     def finished(self):
         if ( self.process_info.remaining_time <= 0.1):
          self.__is_finished = True

         else:
             self.__is_finished = False
        
    
        
