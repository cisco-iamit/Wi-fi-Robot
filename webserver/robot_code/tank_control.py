from .tank_GPIO import RobotDriver, RobotSensors
import time
class RobotController:

    def __init__(self):
        self.robot = RobotDriver()
        self.sensors = RobotSensors()
        self.autoMode = False

    def forward(self):
        self.robot.left_motor_forward()
        self.robot.right_motor_forward()
        print("forward")

    def left(self):
        self.robot.left_motor_backward()
        self.robot.right_motor_forward()
        print("left")

    def right(self):
        self.robot.right_motor_backward()
        self.robot.left_motor_forward()
        print("right")

    def backward(self):
        self.robot.left_motor_backward()
        self.robot.right_motor_backward()
        print("backward")

    def stop(self):
        self.robot.left_motor_stop()
        self.robot.right_motor_stop()
        print("stop")

    def move_automatically(self):
        while self.autoMode:
            if self.sensors.read_left_sensor() == 1:
                self.right()
            elif self.sensors.read_right_sensor() == 1:
    	        self.left()
    	    elif self.sensors.read_front_sensor() == 1:
                self.backward()
            else:
                self.forward()
    	    time.sleep(0.1)

    def set_automode_off(self):
        self.autoMode = off
