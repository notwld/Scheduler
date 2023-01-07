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

q = 4 # Quantum Time
t = 0 # Current Time

nprocess = int(input("Enter the number of processes: "))
bt_rem = [] # Burst Time Remaining

for i in range(nprocess):
    bt = int(input("Enter the burst time for P[{}]: ".format(i+1)))
    bt_rem.append(bt)

ct = [0 for i in range(nprocess)]

temp = bt_rem.copy()

waiting_time = []
turnaround_time = []

while 1:
    done = True
    for i in range(0, 3):
        if bt_rem[i] > 0:
            done = False
            if bt_rem[i] > q:
                t += q
                bt_rem[i] -= q
            else:
                t += bt_rem[i]
                ct[i] = t
                bt_rem[i] = 0

    if done == True:
        break



table.add_column("PId", justify="center")
table.add_column("Arrival Time", justify="center")
table.add_column("BurstTime", justify="center")
table.add_column("CompletionTime", justify="center")
table.add_column("TurnAround Time", justify="center")
table.add_column("Waiting Time", justify="center")

for i in range(0, 3):
    table.add_row(str(i+1), str(0), str(temp[i]), str(ct[i]), str(ct[i]-0), str(ct[i]-temp[i]))
    waiting_time.append(ct[i]-temp[i])
    turnaround_time.append(ct[i]-0)

console.print(table)

print("Avg Waiting Time:", round(sum(waiting_time)/3, 2))
print("Avg TurnAround Time:", round(sum(turnaround_time)/3, 2))