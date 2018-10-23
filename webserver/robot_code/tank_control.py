from .tank_GPIO import RobotDriver

class RobotController:

    def __init__(self):
        self.robot = RobotDriver()

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
