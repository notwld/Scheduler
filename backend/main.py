from algorithms import *
from flask import Flask, request, jsonify

from flask import render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Welcome to Scheduler"


@app.route("/fcfs", methods=["GET"])
def fcfs():
    processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5]]
    scheduler = FCFS(processes)
    return jsonify(scheduler.output())


@app.route("/sjf", methods=["GET"])
def sjf():
    processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5]]
    scheduler = SJF(processes)
    return jsonify(scheduler.output())


@app.route("/rr", methods=["GET"])
def rr():
    processes = [['P1', 0, 8, 2], ['P2', 1, 4, 1],
                 ['P3', 2, 9, 3], ['P4', 3, 5, 4]]
    scheduler = RoundRobin(processes, 4)
    return jsonify(scheduler.output())


@app.route("/priority", methods=["GET"])
def priority():
    processes = [
        Process("P1", 0, 5, 3),
        Process("P2", 2, 2, 1),
        Process("P3", 3, 3, 2),
        Process("P4", 5, 1, 2)
    ]

    scheduler = PriorityScheduler(processes)
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


app.run(debug=True)
