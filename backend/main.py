from algorithms import *
from thread_algo import *
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import render_template
from time import time
app = Flask(__name__)
CORS(app)

app.config["Allow_Headers"] = "*"
app.config["Allow_Methods"] = "*"
app.config["Allow_Origin"] = "*"

def dictionary_to_list(processes):
    process_list = []
    for process in processes:
            process_list.append([int(process['name'].split('P')[1]), int(process['arrivalTime']), int(process['burstTime'])])
    return process_list

def process_to_list(processes):
    process_list = []
    for process in processes:
        process_list.append(Process(int(process['name'].split('P')[1]), int(process['arrivalTime']), int(process['burstTime']), int(process['priority'])))
    return process_list



@app.route("/", methods=["GET"])
def index():
    return "Welcome to Scheduler"


@app.route("/fcfs", methods=["POST"])
def fcfs():
    processes = request.get_json()
    processes = dictionary_to_list(processes)
    print("starting fcfs")
    start = time()
    scheduler = FCFS(processes)
    end = time()
    print(end - start)
    return jsonify(scheduler.output())



@app.route("/sjf", methods=["POST"])
def sjf():
    processes = request.get_json()
    processes = dictionary_to_list(processes)
    scheduler = SJF(processes)
    return jsonify(scheduler.output())


@app.route("/rr", methods=["POST"])
def rr():
    data = request.json
    processes = dictionary_to_list(data['processes'])
    quantum = data['quantum']
    scheduler = RoundRobin(processes, int(quantum))
    return jsonify(scheduler.output())


@app.route("/priority", methods=["POST"])
def priority():
    processes = request.get_json()
    processes = process_to_list(processes)
    scheduler = PriorityScheduler(processes)
    return jsonify(scheduler.output())

@app.route("/fcfs-threaded", methods=["POST"])
def thread_fcfs():
    processes = request.get_json()
    processes = dictionary_to_list(processes)
    print("starting threaded fcfs")
    start = time()
    scheduler = ThreadFCFS(processes)
    end = time()
    print(end - start)
    return jsonify(scheduler.output())



@app.route("/sjf-threaded", methods=["POST"])
def thread_sjf():
    processes = request.get_json()
    processes = dictionary_to_list(processes)
    scheduler = ThreadSJF(processes)
    return jsonify(scheduler.output())


@app.route("/rr-threaded", methods=["POST"])
def thread_rr():
    data = request.json
    processes = dictionary_to_list(data['processes'])
    quantum = data['quantum']
    scheduler = ThreadRoundRobin(processes, int(quantum))
    return jsonify(scheduler.output())


@app.route("/priority-threaded", methods=["POST"])
def thread_priority():
    processes = request.get_json()
    processes = process_to_list(processes)
    scheduler = ThreadPriorityScheduler(processes)
    return jsonify(scheduler.output())


#testing apis with jinja2

@app.route("/fcfs_table")
def fcfs_table():
    processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5]]
    scheduler = FCFS(processes)
    output = scheduler.output()
    return render_template("fcfs_table.html", output=output)


@app.route("/sjf_table")
def sjf_table():
    processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5]]
    scheduler = SJF(processes)
    output = scheduler.output()
    return render_template("sjf_table.html", output=output)


@app.route("/priority_table")
def priority_table():
    processes = [
        Process("P1", 0, 5, 3),
        Process("P2", 2, 2, 1),
        Process("P3", 3, 3, 2),
        Process("P4", 5, 1, 2)
    ]

    scheduler = PriorityScheduler(processes)
    output = scheduler.output()
    return render_template("priority_table.html", output=output)


@app.route("/rr_table")
def rr_table():
    processes = [['P1', 0, 8, 2], ['P2', 1, 4, 1],
                 ['P3', 2, 9, 3], ['P4', 3, 5, 4]]
    scheduler = RoundRobin(processes, 4)
    output = scheduler.output()
    return render_template("rr_table.html", output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)