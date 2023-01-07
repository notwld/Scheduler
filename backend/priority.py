import os

try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    os.system("pip install rich")
    from rich.console import Console
    from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold magenta")

os.system("cls")
n = int(input("Enter the number of processes: "))
processes = []
CT = []
TAT = []
WT = []
for i in range(n):
    b = int(input("Burst Time: "))
    pr = int(input("Priority no: "))
    processes.append(["P"+str(i+1), 0, b, pr])

# sort According to prioriry
processes.sort(key=lambda x: x[3])
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


table.add_column("PId", justify="center")
table.add_column("Arrival Time", justify="center")
table.add_column("BurstTime", justify="center")
table.add_column("Priority", justify="center")
table.add_column("CompletionTime", justify="center")
table.add_column("TurnAround Time", justify="center")
table.add_column("Waiting Time", justify="center")

for i in range(len(processes)):
    table.add_row(str(i+1), str(processes[i][1]), str(processes[i][2]), str(processes[i][3]), str(CT[i]), str(TAT[i]), str(WT[i]))

console.print(table)

print("Avarege TAT: ", round(sum(TAT)/len(TAT), 2))
print("Avarege WT: ", round(sum(WT)/len(WT), 2))
