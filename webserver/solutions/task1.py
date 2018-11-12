from  robot_code.tank_control import RobotController
import time

robot = RobotController()

def run():

    while True:
        sensor_front_val = robot.sensors.read_front_sensor()
        print("Front sensor: {}".format(sensor_front_val))

        if sensor_front_val == 0:
            robot.stop()
        else:
            robot.forward()


        time.sleep(0.2)


try:
    run()
except KeyboardInterrupt:
    robot.stop()
    raise
