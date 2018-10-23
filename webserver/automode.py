from  robot_code.tank_control import RobotController as controller
import time

robot = controller()
while(1):
    sensor_left_val = robot.sensors.read_left_sensor()
    print("Left: {}".format(sensor_left_val))
    time.sleep(1)
