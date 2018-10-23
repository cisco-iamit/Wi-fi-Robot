from  robot_code.tank_control import RobotController as controller
import time

robot = controller()
while(1):
    sensor_left_val = robot.sensors.read_left_sensor()
    if(sensor_left_val == 0):
        robot.turnRight()
    else:
        robot.forward()

    print("Left: {}".format(sensor_left_val))
