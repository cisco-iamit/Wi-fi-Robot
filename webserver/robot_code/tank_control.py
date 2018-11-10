from .tank_GPIO import RobotDriver, RobotSensors
import time
class RobotController:

    def __init__(self):
        self.robot = RobotDriver()
        self.sensors = RobotSensors()

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

    def set_pins(self, pins):
        left_motor_1 = int(pins['left_motor_1'])
        left_motor_2 = int(pins['left_motor_2'])
        right_motor_1 = int(pins['right_motor_1'])
        right_motor_2 = int(pins['right_motor_2'])

        self.robot.set_left_motor_pin_1(left_motor_1)
        self.robot.set_left_motor_pin_2(left_motor_2)
        self.robot.set_right_motor_pin_1(right_motor_1)
        self.robot.set_right_motor_pin_2(right_motor_2)

    def get_pins(self):
        pins = {
            'left_motor_pin_1' : self.robot.left_motor_pin_1,
            'left_motor_pin_2' : self.robot.left_motor_pin_2,
            'right_motor_pin_1' : self.robot.right_motor_pin_1,
            'right_motor_pin_2' : self.robot.right_motor_pin_2
        }
        return pins
