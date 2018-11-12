from  robot_code.tank_control import RobotController
import time

robot = RobotController()

def run():

    while True:
        sensor_front_val = robot.sensors.read_front_sensor()

        if sensor_left_val == 0:
            robot.left()
        else:
            robot.forward()


        time.sleep(0.2)


try:
    run()
except KeyboardInterrupt:
    robot.stop()
    raise
