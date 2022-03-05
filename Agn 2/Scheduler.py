import time
import queue
import os 

global startTime
waitingProcess = []  #List of processes in waiting queue 
readyProcess =[]     #List of processes in ready queue


def current_milli_time():
    return round(time.time() * 1000)

def totalTime():
    return os.current_milli_time() - startTime
# check the total time since the scheduler began
def  isComplete():
    if waitingProcess == 0 & readyProcess == 0:
        return True
    else: 
        return False
    #Check if all procceses have been completed 


def nextProcess():
    for x in  (0, readyProcess.size()):
    #Finding a process with the smallest remaining time to be executed 


def waitingList():
    if waitingProcess == 0:
        
    #When a process is ready it goes to the ready queue and is excecuted
    #Moving from waiting to ready queue
    #Increament the waiting time based on how long it has been waiting 


def scheduler(self, process):
   startTime = os.current_milli_time()
    #Implement clock here





