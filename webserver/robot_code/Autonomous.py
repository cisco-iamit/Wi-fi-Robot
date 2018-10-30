#!/usr/bin/env python3
from tank_control import RobotController
import time

controller = RobotController()

while True:
    if controller.sensors.read_left_sensor() == 1:
        controller.right()
    elif controller.sensors.read_right_sensor() == 1:
        controller.left()
    elif controller.sensors.read_front_sensor() == 1:
        controller.backward()
    else:
        C.forward()
