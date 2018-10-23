from flask import Flask, render_template
app = Flask(__name__, template_folder='.')
from  robot_code.tank_control import RobotController as controller

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/move_forward', methods=['GET'])
def move_forward():
    controller().forward()
    print("Forward called")
    return "Forward"

@app.route('/turn_left', methods=['GET'])
def turn_left():
    controller().left()
    print("Left called")
    return "Left"

@app.route('/turn_right', methods=['GET'])
def turn_right():
    controller().right()
    print("Right called")
    return "Right"

@app.route('/move_back', methods=['GET'])
def move_back():
    controller().back()
    print("Back called")
    return "Back"

@app.route('/stop', methods=['GET'])
def move_stop():
    controller().stop()
    print("Stop called")
    return "Stop"

if __name__ == "__main__":
    #app = Flask(__name__, template_folder='.')
    app.run(host='0.0.0.0', port=8000, debug=True)
