from flask import Flask, render_template
import random


app = Flask(__name__, template_folder='.')
from  robot_code.tank_control import RobotController as controller

controller = controller()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/move_forward', methods=['GET'])
def move_forward():
    controller.forward()
    print("Forward called")
    return "Forward"

@app.route('/turn_left', methods=['GET'])
def turn_left():
    controller.left()
    print("Left called")
    return "Left"

@app.route('/turn_right', methods=['GET'])
def turn_right():
    controller.right()
    print("Right called")
    return "Right"

@app.route('/move_back', methods=['GET'])
def move_back():
    controller.backward()
    print("Back called")
    return "Back"

@app.route('/stop', methods=['GET'])
def move_stop():
    controller.stop()
    print("Stop called")
    return "Stop"

@app.route('/query_proximity_sensor/<position>', methods=['GET'])
def get_sensor_reading(position):
    ## Logic to query sensors!
    if position == "left":
        return str(controller.sensors.read_left_sensor())
    elif position == "right":
        return str(controller.sensors.read_right_sensor())
    elif position == "front":
        return str(controller.sensors.read_front_sensor())
    return "failed"


#@app.route('/set_autopilot_on', methods=['GET'])
#def set_autopilot_mode_on():
#    subprocess.run(['python','robot_code/Autonomous.py'])
#
#   return "set autopilot on"
#
#@app.route('/set_autopilot_off', methods=['GET'])
#def set_autopilot_mode_off():
#    current_process = psutil.Process()
#    children = current_process.children(recursive=True)
#    for child in children:
#        print('Child pid is {}'.format(child.pid))
#        subprocess.run(['pkill', child.pid])
#    return "set autopilot off"

if __name__ == "__main__":
    #app = Flask(__name__, template_folder='.')
    app.run(host='0.0.0.0', port=8000, debug=True)
