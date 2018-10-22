from GPIO2 import RobotDriver

g = RobotDriver()

def forward(g):
    g.left_motor_forward()
    g.right_motor_forward()
    print("forward")


def left(g):
    g.left_motor_backward()
    g.right_motor_forward()
    print("left")


def right(g):
    g.right_motor_backward()
    g.left_motor_forward()
    print("right")


def backward(g):
    g.left_motor_backward()
    g.right_motor_backward()
    print("backward")


def stop(g):
    g.left_motor_stop()
    g.right_motor_stop()
    print("stop")
