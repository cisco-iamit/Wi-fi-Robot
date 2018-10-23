#!/usr/bin/env python3
import .tank_GPIO
import time

C = RobotDriver()
S = RobotSensors()


while True:
    if S.read_left_sensor() == 1:
        C.right_motor_backward()
    if S.read_front_sensor() == 1:
        C.left_motor_backward()
        C.right_motor_backward()
    if S.read_right_sensor() == 1:
        C.left_motor_backward()
    else:
        C.left_motor_forward()
        C.right_motor_forward()
    time.sleep(0.1)
