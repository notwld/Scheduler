class Process:
  def __init__(self, name, arrival_time, burst_time, priority):
    self.name = name
    self.arrival_time = arrival_time
    self.burst_time = burst_time
    self.priority = priority 
    self.start_time = 0
    self.finish_time = 0
    self.turnaround_time=[]
    self.waiting_time=[]

from abc import ABC, abstractmethod

class Scheduler(ABC):
    def __init__(self):
        self.PROCESSES = []
        self.BT = []
        self.CT = []
        self.TAT = []
        self.WT = []
        self.AT = []
        self.PN = []
        self.PR=[]
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
        for i in range(len(self.PROCESSES)):
            self.AT.append(self.PROCESSES[i][1])
            self.BT.append(self.PROCESSES[i][2])
            self.PN.append(self.PROCESSES[i][0])
    

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
        "Process Name": self.PN,
        "Arrival Time": self.AT,
        "Burst Time": self.BT,
        "Completion Time": self.CT,
        "Turnaround Time": self.TAT,
        "Waiting Time": self.WT,
        "AVG Waiting Time": self.CALCULATE_AVG_WT(),
        "AVG Turnaround Time": self.CALCULATE_AVG_TAT()
        }


class SJF(Scheduler):
    def __init__(self, processes: list):
        super().__init__()
        self.PROCESSES = processes
        self.PROCESSES.sort(key=lambda x: (x[1], x[2]))
        for i in range(len(self.PROCESSES)):
            self.AT.append(self.PROCESSES[i][1])
            self.BT.append(self.PROCESSES[i][2])
            self.PN.append(self.PROCESSES[i][0])

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
        "Process Name": self.PN,
        "Arrival Time": self.AT,
        "Burst Time": self.BT,
        "Completion Time": self.CT,
        "Turnaround Time": self.TAT,
        "Waiting Time": self.WT,
        "AVG Waiting Time": self.CALCULATE_AVG_WT(),
        "AVG Turnaround Time": self.CALCULATE_AVG_TAT()
        }




class PriorityScheduler(Scheduler):
    def __init__(self, processes: list):
        super().__init__()
        self.PROCESSES = processes
        
        self.PROCESSES.sort(key=lambda x: x.priority, reverse=True)
        for i in range(len(self.PROCESSES)):
            self.AT.append(self.PROCESSES[i].arrival_time)
            self.BT.append(self.PROCESSES[i].burst_time)
            self.PN.append(self.PROCESSES[i].name)
            self.PR.append(self.PROCESSES[i].priority)

    def priority_scheduling(self):
        current_time = self.PROCESSES[0].arrival_time
        for process in self.PROCESSES:
            process.start_time = current_time
            current_time += process.burst_time
            process.finish_time = current_time

    def CALCULATE_CT(self):
        self.priority_scheduling()
        for process in self.PROCESSES:
            self.CT.append(process.finish_time)

    def CALCULATE_TAT(self):
        for i in range(len(self.PROCESSES)):
            self.TAT.append(self.CT[i]-self.PROCESSES[i].arrival_time)

    def CALCULATE_WT(self):
        for i in range(len(self.PROCESSES)):
            self.WT.append(self.TAT[i]-self.PROCESSES[i].burst_time)

    def CALCULATE_AVG_WT(self):
        return round(sum(self.WT)/len(self.WT), 2)

    def CALCULATE_AVG_TAT(self):
        return round(sum(self.TAT)/len(self.TAT), 2)

    def output(self):
        self.CALCULATE_CT()
        self.CALCULATE_TAT()
        self.CALCULATE_WT()
        return {
        "Process Name": self.PN,
        "Arrival Time": self.AT,
        "Burst Time": self.BT,
        "Priority No": self.PR,
        "Start Time": [p.start_time for p in self.PROCESSES],
        "Completion Time": self.CT,
        "Turnaround Time": self.TAT,
        "Waiting Time": self.WT,
        "AVG Waiting Time": self.CALCULATE_AVG_WT(),
        "AVG Turnaround Time": self.CALCULATE_AVG_TAT()
        }

class RoundRobin(Scheduler):
    def __init__(self, processes: list,q):
        super().__init__()
        self.PROCESSES = processes
        self.q = q
        self.BT_rem = []
        self.CT = [0 for i in range(len(self.PROCESSES))]
        self.temp = []
        self.AT = []
        self.PN = []

        for i in range(len(self.PROCESSES)):
            self.AT.append(self.PROCESSES[i][1])
            self.BT.append(self.PROCESSES[i][2])
            self.PN.append(self.PROCESSES[i][0])
            self.BT_rem.append(self.PROCESSES[i][2])
            self.temp.append(self.PROCESSES[i][2])

    def CALCULATE_CT(self):
        t = 0
        done = False

        while not done:
            done = True
            for i in range(len(self.PROCESSES)):
                if self.BT_rem[i] > 0:
                    done = False
                    if self.BT_rem[i] > self.q:
                        t += self.q
                        self.BT_rem[i] -= self.q
                    else:
                        t = t + self.BT_rem[i]
                        self.CT[i] = t
                        self.BT_rem[i] = 0

        return self.CT

    def CALCULATE_TAT(self):
        for i in range(len(self.PROCESSES)):
            self.TAT.append(self.CT[i] - self.AT[i])

    def CALCULATE_WT(self):
        for i in range(len(self.PROCESSES)):
            self.WT.append(self.TAT[i] - self.temp[i])

    def CALCULATE_AVG_WT(self):
        return round(sum(self.WT) / len(self.WT), 2)

    def CALCULATE_AVG_TAT(self):
        return round(sum(self.TAT) / len(self.TAT), 2)

    def output(self):
        self.CALCULATE_CT()
        self.CALCULATE_TAT()
        self.CALCULATE_WT()
        return {
            "Process Name": self.PN,
            "Arrival Time": self.AT,
            "Burst Time": self.temp,
            "Time Quantum": self.q,
            "Completion Time": self.CT,
            "Turnaround Time": self.TAT,
            "Waiting Time": self.WT,
            "AVG Waiting Time": self.CALCULATE_AVG_WT(),
            "AVG Turnaround Time": self.CALCULATE_AVG_TAT()
        }
    

# print("Round Robin")
# processes = [['P1', 0, 8, 2], ['P2', 1, 4, 1], ['P3', 2, 9, 3], ['P4', 3, 5, 4]]
# rr_scheduler = RoundRobin(processes,4)
# output3 = rr_scheduler.output()
# print(output3)
# print("Process Name:", output3["Process Name"])
# print("Arrival Time:", output3["Arrival Time"])
# print("Time Quantum:",output3["Time Quantum"])
# print("Burst Time:", output3["Burst Time"])
# print("Completion Time:", output3["Completion Time"])
# print("Turnaround Time:", output3["Turnaround Time"])
# print("Waiting Time:", output3["Waiting Time"])
# print("AVG Waiting Time:", output3["AVG Waiting Time"])
# print("AVG Turnaround Time:", output3["AVG Turnaround Time"])


# # Creating a list of processes with their Process Number, arrival time and burst time.
# #FCFS
# processes = [("p1", 0, 4), ("p2", 1, 2), ("p3", 2, 1)]
# scheduler = FCFS(processes)
# result = scheduler.output()
# print("FCFS: ",result)

# #SJF
# processes1 = [("p1", 3, 3), ("p2", 1, 2), ("p3", 0, 1)]
# scheduler1 = SJF(processes1)
# result1 = scheduler1.output()
# print("SJF: ",result1)

# processes = [
#     Process("P1", 0, 5, 3), 
#     Process("P2", 2, 2, 1),  
#     Process("P3", 3, 3, 2),
#     Process("P4", 5, 1, 2) 
# ]

# scheduler = PriorityScheduler(processes)
# results = scheduler.output()

# # print("Priorty: ",results)
# print()
# print("Priority")
# print("Process Name:", results["Process Name"])
# print("Arrival Time:", results["Arrival Time"])
# print("Burst Time:", results["Burst Time"])
# print("Priority:",results["Priority No"])
# print("Start Time:", results["Start Time"])
# print("Completion Time:", results["Completion Time"])
# print("Turnaround Time:", results["Turnaround Time"])
# print("Waiting Time:", results["Waiting Time"])
# print("AVG Waiting Time:", results["AVG Waiting Time"])
# print("AVG Turnaround Time:", results["AVG Turnaround Time"])

