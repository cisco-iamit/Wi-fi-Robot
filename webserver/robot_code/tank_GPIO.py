import RPi.GPIO as GPIO
import time

class RobotDriver():
    
    def __init__(self,
    	left_motor_pin_1=16,
    	left_motor_pin_2=19,
    	right_motor_pin_1=26,
    	right_motor_pin_2=20):

        self.left_motor_pin_1 = left_motor_pin_1
        self.left_motor_pin_2 = left_motor_pin_2
        self.right_motor_pin_1 = right_motor_pin_1
        self.right_motor_pin_2 = right_motor_pin_2

        self.init_pins()

    def init_pins(self):
        GPIO.setmode(GPIO.BCM)              #set pin mode
        GPIO.setwarnings(False)             #turns off power limt warnings
        #left motor
        GPIO.setup(self.left_motor_pin_1,GPIO.OUT)
        GPIO.setup(self.left_motor_pin_2,GPIO.OUT)
        #right motor
        GPIO.setup(self.right_motor_pin_1,GPIO.OUT)
        GPIO.setup(self.right_motor_pin_2,GPIO.OUT)


    def left_motor_forward(self):
        GPIO.output(self.left_motor_pin_1,GPIO.HIGH)
        GPIO.output(self.left_motor_pin_2,GPIO.LOW)

    def left_motor_backward(self):
        GPIO.output(self.left_motor_pin_1,GPIO.LOW)
        GPIO.output(self.left_motor_pin_2,GPIO.HIGH)

    def left_motor_stop(self):
        GPIO.output(self.left_motor_pin_1,GPIO.LOW)
        GPIO.output(self.left_motor_pin_2,GPIO.LOW)



    def right_motor_forward(self):
        GPIO.output(self.right_motor_pin_1,GPIO.HIGH)
        GPIO.output(self.right_motor_pin_2,GPIO.LOW)

    def right_motor_backward(self):
        GPIO.output(self.right_motor_pin_1,GPIO.LOW)
        GPIO.output(self.right_motor_pin_2,GPIO.HIGH)

    def right_motor_stop(self):
        GPIO.output(self.right_motor_pin_1,GPIO.LOW)
        GPIO.output(self.right_motor_pin_2,GPIO.LOW)
