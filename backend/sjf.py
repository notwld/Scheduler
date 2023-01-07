import os
try:
    from rich.console import Console
    from rich.table import Table
except ModuleNotFoundError:
    os.system("pip install rich")
    from rich.console import Console
    from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold magenta")
os.system("cls")

nprocess = int(input("Enter number of processes: "))
processes = []
CT = []
TAT = []
WT = []
for i in range(nprocess):
    b = int(input("Burst Time: "))
    processes.append(["P"+str(i+1), 0, b])

# sort According to burst time
processes.sort(key=lambda x: x[2])

# Calculting Completion time
for i in range(len(processes)):
    if i == 0:
        if processes[i][1] > 0:
            state_idle = processes[i][1]
            CT.append(processes[i][2]+state_idle)
        else:
            CT.append(processes[i][2])
    else:
        if CT[i-1] < processes[i][1]:
            idle_state = processes[i][1] - CT[i-1]
            CT.append(CT[i-1]+processes[i][2]+idle_state)
        else:
            CT.append(CT[i-1]+processes[i][2])

# Calculation Turn Around Time
for i in range(len(processes)):
    TAT.append(CT[i]-processes[i][1])

# Calculation Waiting Time
for i in range(len(processes)):
    WT.append(TAT[i]-processes[i][2])

table.add_column("Process", justify="center")
table.add_column("Arrival Time", justify="center")
table.add_column("Burst Time", justify="center")
table.add_column("Completion Time", justify="center")
table.add_column("Turn Around Time", justify="center")
table.add_column("Waiting Time", justify="center")

for i in range(len(processes)):
    table.add_row(str(processes[i][0]), str(processes[i][1]), str(
        processes[i][2]), str(CT[i]), str(TAT[i]), str(WT[i]))


console.print(table)

print("Avarege TAT: ", round(sum(TAT)/len(TAT), 2))
print("Avarege WT: ", round(sum(WT)/len(WT), 2))
