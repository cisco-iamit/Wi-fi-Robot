# IamIT Wi-Fi Robot

## Installation

Prerequisites:
- Python 3 (check this using `python --version` or `python3 --version`)
- Flask (`pip install flask`)
- RPi module (this should be installed by default)

Set up:
1) SSH into the Pi or open a terminal on the Desktop GUI and use these commands:
```shell
# Download the repository
git clone https://github.com/cisco-iamit/Wi-fi-Robot.git

# Change directory into the webserver folder
cd Wi-fi-Robot/webserver

# Run the web client (assuming python3 is installed)
python server.py
```

## The Web Client

Once you have run `python server.py`, you should be able to view
the webserver on the IP address of the Pi, `port 8000`.

For example, if the IP address of your Pi is `192.168.43.211`, visit `192.168.43.211:8000` on your web browser (the laptop must be connected on the same network!)

In the web client you can see the sensor readings from the robot and control the robot using the arrow keys! You can also click on the arrows to move them!

## Robot API

The robot can be controlled through the `RobotController` class.

Importing the `RobotController` class can be done using:
```python
from robot_code.tank_control import RobotController as controller

robot_control = RobotController()
```

### Moving the Robot

You can call these methods on your initialised `RobotController` instance to move the robot.

```python
# Go forward
robot_control.forward()

# Go backward
robot_control.backward()

# Turn left
robot_control.left()

# Turn right
robot_control.right()

# To stop
robot_control.stop()
```

### Reading the sensor input

There are three IR sensors provided and the values can be read as so:

Note that the function returns an Integer 0 or 1, where 0 is if there is an object infront of the sensor and 1 if there is not

```python
# Read left sensor
robot_control.sensors.read_left_sensor()
# Read right sensor
robot_control.sensors.read_right_sensor()
# Read front sensor
robot_control.sensors.read_front_sensor()
```

It's best to use this in a while loop (with some timeout).
