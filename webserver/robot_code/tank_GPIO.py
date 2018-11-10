import RPi.GPIO as GPIO
import time

class RobotSensors():

    def __init__(self,
        sensor_left_pin=2,
        sensor_front_pin=3,
        sensor_right_pin=4
    ):

        self.sensor_left_pin = sensor_left_pin
        self.sensor_front_pin = sensor_front_pin
        self.sensor_right_pin = sensor_right_pin

        self.init_pins()

    def init_pins(self):
        GPIO.setmode(GPIO.BCM)              #set pin mode
        GPIO.setwarnings(False)
        GPIO.setup(self.sensor_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.sensor_front_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.sensor_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_left_sensor(self):
        val = GPIO.input(self.sensor_left_pin)
        return val

    def read_front_sensor(self):
        val = GPIO.input(self.sensor_front_pin)
        return val

    def read_right_sensor(self):
        val = GPIO.input(self.sensor_right_pin)
        return val

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

            self.valid_pins = [16,19,26,20]
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

    def set_left_motor_pin_1(self, pin):
        if pin in self.valid_pins:
            self.left_motor_pin_1 = pin

    def set_left_motor_pin_2(self, pin):
        if pin in self.valid_pins:
            self.left_motor_pin_2 = pin

    def set_right_motor_pin_1(self, pin):
        if pin in self.valid_pins:
            self.right_motor_pin_1 = pin

    def set_right_motor_pin_2(self, pin):
        if pin in self.valid_pins:
            self.right_motor_pin_2 = pin
