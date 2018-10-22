import RPi.GPIO as GPIO
import time



class RobotDriver():

    def __init__(self,
    left_motor_pin_1=26,
    left_motor_pin_2=20,
    right_motor_pin_1=19,
    right_motor_pin_2=17):

        self.left_motor_pin_1 = left_motor_pin_1
        self.left_motor_pin_2 = left_motor_pin_2
        self.right_motor_pin_1 = right_motor_pin_1
        self.right_motor_pin_2 = right_motor_pin_2

        init_pins()

    def init_pins():
        GPIO.setmode(GPIO.BCM)              #set pin mode
        GPIO.setwarnings(False)             #turns off power limt warnings
        #left motor
        GPIO.setup(self.left_motor_pin_1,GPIO.OUT)
        GPIO.setup(self.left_motor_pin_2,GPIO.OUT)
        #right motor
        GPIO.setup(self.right_motor_pin_1,GPIO.OUT)
        GPIO.setup(self.right_motor_pin_2,GPIO.OUT)


    def left_motor_forward():
        GPIO.output(self.left_motor_pin_1,GPIO.high)
        GPIO.output(self.left_motor_pin_1,GPIO.low)

    def left_motor_backward():
        GPIO.output(self.right_motor_pin_1,GPIO.low)
        GPIO.output(self.right_motor_pin_2,GPIO.high)

    def right_motor_stop():
        GPIO.output(self.right_motor_pin_1,GPIO.low)
        GPIO.output(self.right_motor_pin_2,GPIO.low)



    def right_motor_forward():
        GPIO.output(26,GPIO.high)
        GPIO.output(20,GPIO.low)

    def right_motor_backward():
        GPIO.output(26,GPIO.low)
        GPIO.output(20,GPIO.high)

    def right_motor_stop():
        GPIO.output(26,GPIO.low)
        GPIO.output(20,GPIO.low)
