from abc import ABC, abstractmethod

class Scheduler(ABC):
    def __init__(self):
        self.PROCESSES = []
        self.BT = []
        self.CT = []
        self.TAT = []
        self.WT = []
    
    @abstractmethod
    def CALCULATE_CT(self):
        pass
    
    @abstractmethod
    def CALCULATE_TAT(self):
        pass

    @abstractmethod
    def CALCULATE_WT(self):
        pass

    @abstractmethod
    def CALCULATE_AVG_WT(self):
        pass

    @abstractmethod
    def CALCULATE_AVG_TAT(self):
        pass

class FCFS(Scheduler):
    def __init__(self,processes: list):
        super().__init__()
        self.PROCESSES = processes
        self.PROCESSES.sort(key=lambda x: x[1])
    
    def CALCULATE_CT(self):
        for i in range(len(self.PROCESSES)):
            if i == 0:
                if self.PROCESSES[i][1] > 0:
                    state_idle = self.PROCESSES[i][1]
                    self.CT.append(self.PROCESSES[i][2]+state_idle)
                else:
                    self.CT.append(self.PROCESSES[i][2])
            else:
                if self.CT[i-1] < self.PROCESSES[i][1]:
                    idle_state = self.PROCESSES[i][1] - self.CT[i-1]
                    self.CT.append(self.CT[i-1]+self.PROCESSES[i][2]+idle_state)
                else:
                    self.CT.append(self.CT[i-1]+self.PROCESSES[i][2])
        return self.CT

    def CALCULATE_TAT(self):
        for i in range(len(self.PROCESSES)):
            self.TAT.append(self.CT[i]-self.PROCESSES[i][1])

    def CALCULATE_WT(self):
        for i in range(len(self.PROCESSES)):
            self.WT.append(self.TAT[i]-self.PROCESSES[i][2])

    def CALCULATE_AVG_WT(self):
        return round(sum(self.WT)/len(self.WT), 2)

    def CALCULATE_AVG_TAT(self):
        return round(sum(self.TAT)/len(self.TAT), 2)

    def output(self):
        self.CALCULATE_CT()
        self.CALCULATE_TAT()
        self.CALCULATE_WT()
        return {
            "CT": self.CT,
            "TAT": self.TAT,
            "WT": self.WT,
            "AVG_WT": self.CALCULATE_AVG_WT(),
            "AVG_TAT": self.CALCULATE_AVG_TAT()
        }

class SJF(Scheduler):
    def __init__(self, processes: list):
        super().__init__()
        self.PROCESSES = processes
        self.PROCESSES.sort(key=lambda x: (x[1], x[2]))

    def CALCULATE_CT(self):
        self.CT = [0] * len(self.PROCESSES)
        for i in range(len(self.PROCESSES)):
            if i == 0:
                self.CT[i] = self.PROCESSES[i][1] + self.PROCESSES[i][2]
            else:
                if self.CT[i-1] < self.PROCESSES[i][1]:
                    self.CT[i] = self.PROCESSES[i][1] + self.PROCESSES[i][2]
                else:
                    self.CT[i] = self.CT[i-1] + self.PROCESSES[i][2]
        return self.CT

    def CALCULATE_TAT(self):
        for i in range(len(self.PROCESSES)):
            self.TAT.append(self.CT[i]-self.PROCESSES[i][1])

    def CALCULATE_WT(self):
        for i in range(len(self.PROCESSES)):
            self.WT.append(self.TAT[i]-self.PROCESSES[i][2])

    def CALCULATE_AVG_WT(self):
        return round(sum(self.WT)/len(self.WT), 2)

    def CALCULATE_AVG_TAT(self):
        return round(sum(self.TAT)/len(self.TAT), 2)

    def output(self):
        self.CALCULATE_CT()
        self.CALCULATE_TAT()
        self.CALCULATE_WT()
        return {
            "CT": self.CT,
            "TAT": self.TAT,
            "WT": self.WT,
            "AVG_WT": self.CALCULATE_AVG_WT(),
            "AVG_TAT": self.CALCULATE_AVG_TAT()
        }
class RoundRobin(Scheduler):
    def __init__(self, processes: list, quantum: int):
        super().__init__()
        self.PROCESSES = processes
        self.QUANTUM = quantum
        self.BT = [i[2] for i in self.PROCESSES]
        self.PROCESS_ID = [i[0] for i in self.PROCESSES]
        self.WT = [0] * len(self.PROCESSES)
        self.TAT = [0] * len(self.PROCESSES)
        self.CT = [0] * len(self.PROCESSES)
        self.RT = [i for i in self.BT]
    
    def CALCULATE_CT(self):
        t = 0
        while(True):
            done = True
            for i in range(len(self.PROCESSES)):
                if self.RT[i] > 0:
                    done = False
                    if self.RT[i] > self.QUANTUM:
                        t += self.QUANTUM
                        self.RT[i] -= self.QUANTUM
                    else:
                        t = t + self.RT[i]
                        self.WT[i] = t - self.BT[i]
                        self.RT[i] = 0
            if done == True:
                break
        self.CT = [self.WT[i] + self.BT[i] for i in range(len(self.PROCESSES))]
        return self.CT

    def CALCULATE_TAT(self):
        self.TAT = [self.CT[i] - self.PROCESSES[i][1] for i in range(len(self.PROCESSES))]
        return self.TAT

    def CALCULATE_WT(self):
        return self.WT

    def CALCULATE_AVG_WT(self):
        return round(sum(self.WT)/len(self.WT), 2)

    def CALCULATE_AVG_TAT(self):
        return round(sum(self.TAT)/len(self.TAT), 2)

    def output(self):
        self.CALCULATE_CT()
        self.CALCULATE_TAT()
        return {
            "CT": self.CT,
            "TAT": self.TAT,
            "WT": self.WT,
            "AVG_WT": self.CALCULATE_AVG_WT(),
            "AVG_TAT": self.CALCULATE_AVG_TAT()
        }
        


#
class Priority(Scheduler):
    def __init__(self, processes: list):
        super().__init__()
        self.PROCESSES = processes
        self.PROCESSES.sort(key=lambda x: (x[3], x[1]))

    def CALCULATE_CT(self):
        self.CT = [0] * len(self.PROCESSES)
        for i in range(len(self.PROCESSES)):
            if i == 0:
                self.CT[i] = self.PROCESSES[i][1] + self.PROCESSES[i][2]
            else:
                if self.CT[i-1] < self.PROCESSES[i][1]:
                    self.CT[i] = self.PROCESSES[i][1] + self.PROCESSES[i][2]
                else:
                    self.CT[i] = self.CT[i-1] + self.PROCESSES[i][2]

    def CALCULATE_TAT(self):
        for i in range(len(self.PROCESSES)):
            self.TAT.append(self.CT[i] - self.PROCESSES[i][1])

    def CALCULATE_WT(self):
        for i in range(len(self.PROCESSES)):
            self.WT.append(self.TAT[i] - self.PROCESSES[i][2])

    def CALCULATE_AVG_WT(self):
        return round(sum(self.WT) / len(self.WT), 2)

    def CALCULATE_AVG_TAT(self):
        return round(sum(self.TAT) / len(self.TAT), 2)

    def output(self):
        self.CALCULATE_CT()
        self.CALCULATE_TAT()
        self.CALCULATE_WT()
        return {
            "CT": self.CT,
            "TAT": self.TAT,
            "WT": self.WT,
            "AVG_WT": self.CALCULATE_AVG_WT(),
            "AVG_TAT": self.CALCULATE_AVG_TAT()
        }

#


# # processes = [("P1", 0, 8), ("P2", 1, 4), ("P3", 2, 9), ("P4", 3, 5)]
# # quantum = 3
# # rr = RoundRobin(processes, quantum)
# # print(rr.output())


# # Creating a list of processes with their Process Number, arrival time and burst time.
# processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5]]

# # FCFS instance
# fcfs = FCFS(processes)
# print("FCFS:", fcfs.output())

# # SJF instance
# sjf = SJF(processes)
# print("SJF:", sjf.output())

# # Round Robin instance
# quantum = 2
# rr = RoundRobin(processes, quantum)
# print("Round Robin:", rr.output())


# # Creating a list of processes with their arrival time, burst time and priority
# processes = [("p1", 0, 10, 3), ("p2", 1, 5, 2), ("p3", 2, 8, 1)]

# # Creating an object of the Priority class
# scheduler = Priority(processes)


# output = scheduler.output()
# print("Priority")
# print("Completion Time: ", output["CT"])
# print("Turnaround Time: ", output["TAT"])
# print("Waiting Time: ", output["WT"])
# print("Average Waiting Time: ", output["AVG_WT"])
# print("Average Turnaround Time: ", output["AVG_TAT"])
