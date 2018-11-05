from  robot_code.tank_control import RobotController as controller
import time

robot = controller()
def run():

    while(1):
        sensor_left_val = robot.sensors.read_left_sensor()
        sensor_right_val = robot.sensors.read_right_sensor()
        sensor_front_val = robot.sensors.read_front_sensor()
        
        if sensor_left_val == 0:
            robot.right()
        elif sensor_right_val == 0:
            robot.left()
        elif sensor_front_val == 0:
            robot.backward()
        else:
            robot.forward()

        print("Left: {}".format(sensor_left_val))
        time.sleep(0.2)


try:
    run()
except KeyboardInterrupt:
    robot.stop()
    raise
