from algorithms import *
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return "Welcome to Scheduler"

@app.route("/fcfs",methods=["GET"])
def fcfs():
    processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5]]
    scheduler = FCFS(processes)
    return jsonify(scheduler.output())

app.run(debug=True)