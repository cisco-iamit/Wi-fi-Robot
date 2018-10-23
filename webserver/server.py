from flask import Flask, render_template
app = Flask(__name__, template_folder='.')
from robot_code import RobotController

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/move_forward', methods=['GET'])
def move_forward():
    RobotController().forward()

@app.route('/turn_left', methods=['GET'])
def turn_left():
    RobotController().left()

@app.route('/turn_right', methods=['GET'])
def turn_right():
    RobotController().right()

@app.route('/move_back', methods=['GET'])
def move_back():
    RobotController().back()

@app.route('/stop', methods=['GET'])
def move_back():
    RobotController().stop()
