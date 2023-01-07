from abc import ABC,abstractmethod

class Schedular(ABC):
    PROCESSES: list = []
    BT: list = []
    CT: list = []
    TAT: list = []
    WT: list = []

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


class FCFS(Schedular):
    def __init__(self):
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
        
        return self.TAT

    def CALCULATE_WT(self):
        for i in range(len(self.PROCESSES)):
            self.WT.append(self.TAT[i]-self.PROCESSES[i][2])

        return self.WT

    def CALCULATE_AVG_WT(self):
        return round(sum(self.TAT)/len(self.TAT), 2)

    def CALCULATE_AVG_TAT(self):
        return round(sum(self.WT)/len(self.WT), 2)

def unit_test(processes, wt, tat, ct):
    for i in range(len(processes)):
        print(f"Process: {processes[i][0]}")
        print(f"AT: {processes[i][1]}")
        print(f"BT: {processes[i][2]}")
        print(f"WT: {wt[i]}")
        print(f"TAT: {tat[i]}")
        print(f"CT: {ct[i]}")
        print("")
    print(f"Average WT: {sum(wt)/len(wt)}")
    print(f"Average TAT: {sum(tat)/len(tat)}")
    

if __name__=="__main__":
    strategy = FCFS()
    from random import randint
    strategy.PROCESSES.append(["P"+str(1), randint(1,8),randint(1,8)])
    strategy.PROCESSES.append(["P"+str(2), randint(1,8),randint(1,8)])
    strategy.PROCESSES.append(["P"+str(3), randint(1,8),randint(1,8)])
    strategy.PROCESSES.append(["P"+str(4), randint(1,8),randint(1,8)])
    strategy.PROCESSES.append(["P"+str(5), randint(1,8),randint(1,8)])
    print(strategy.PROCESSES)
    print(strategy.CALCULATE_CT(),
    strategy.CALCULATE_TAT(),
    strategy.CALCULATE_WT(),
    strategy.CALCULATE_AVG_WT(),
    strategy.CALCULATE_AVG_TAT())

    unit_test(strategy.PROCESSES,strategy.WT, strategy.TAT, strategy.CT)
