from  robot_code.tank_control import RobotController as controller
import time

robot = controller()

def run():

    while(1):
        sensor_front_val = robot.sensors.read_front_sensor()
        print("Front sensor: {}".format(sensor_front_pin))

        # Write your code here!


        time.sleep(0.2)


try:
    run()
except KeyboardInterrupt:
    robot.stop()
    raise
