import RPi.GPIO as GPIO
import time

class RobotArm():

    def __init__(self,
    	servo_1=11,
    	servo_2=9,
    	servo_3=10,
    	servo_4=22,
    	servo_5=27,
    	servo_6=17):

            self.servo_1 = servo_1
            self.servo_2 = servo_2
            self.servo_3 = servo_3
            self.servo_4 = servo_4
            self.servo_5 = servo_5
            self.servo_6 = servo_6


    def init_pins(self):
        GPIO.setmode(GPIO.BCM)              #set pin mode
        GPIO.setwarnings(False)             #turns off power limt warnings
        #Claw
        GPIO.setup(self.servo_1,GPIO.OUT)
        self.pwm_servo_1 = GPIO.PWM(self.servo_1, 270)

        GPIO.setup(self.servo_1,GPIO.OUT)
        self.pwm_servo_2 = GPIO.PWM(self.servo_2, 270)

        GPIO.setup(self.servo_1,GPIO.OUT)
        self.pwm_servo_3 = GPIO.PWM(self.servo_3, 270)

        GPIO.setup(self.servo_1,GPIO.OUT)
        self.pwm_servo_4 = GPIO.PWM(self.servo_4, 270)

        GPIO.setup(self.servo_1,GPIO.OUT)
        self.pwm_servo_5 = GPIO.PWM(self.servo_5, 270)

        GPIO.setup(self.servo_1,GPIO.OUT)
        self.pwm_servo_6 = GPIO.PWM(self.servo_6, 270)


    def servo_1_move(self, angle):
        duty = angle / 18 + 2
        self.pwm_servo_1.ChangeDutyCycle(duty)
        self.pwm_servo_1.ChangeDutyCycle(0)
    def servo_2_move(self, angle):
        duty = angle / 18 + 2
        self.pwm_servo_2.ChangeDutyCycle(duty)
        self.pwm_servo_2.ChangeDutyCycle(0)
    def servo_3_move(self, angle):
        duty = angle / 18 + 2
        self.pwm_servo_3.ChangeDutyCycle(duty)
        self.pwm_servo_3.ChangeDutyCycle(0)
    def servo_4_move(self, angle):
        duty = angle / 18 + 2
        self.pwm_servo_4.ChangeDutyCycle(duty)
        self.pwm_servo_4.ChangeDutyCycle(0)
    def servo_5_move(self, angle):
        duty = angle / 18 + 2
        self.pwm_servo_5.ChangeDutyCycle(duty)
        self.pwm_servo_5.ChangeDutyCycle(0)
    def servo_6_move(self, angle):
        duty = angle / 18 + 2
        self.pwm_servo_6.ChangeDutyCycle(duty)
        self.pwm_servo_6.ChangeDutyCycle(0)



    def servo_1_stop():
        self.pwm_servo_1.stop()
    def servo_2_stop():
        self.pwm_servo_2.stop()
    def servo_3_stop():
        self.pwm_servo_3.stop()
    def servo_4_stop():
        self.pwm_servo_4.stop()
    def servo_5_stop():
        self.pwm_servo_5.stop()
    def servo_6_stop():
        self.pwm_servo_6.stop()


    def servo_1_stop():
        self.pwm_servo_1.stop()
    def servo_2_stop():
        self.pwm_servo_2.stop()
    def servo_3_stop():
        self.pwm_servo_3.stop()
    def servo_4_stop():
        self.pwm_servo_4.stop()
    def servo_5_stop():
        self.pwm_servo_5.stop()
    def servo_6_stop():
        self.pwm_servo_6.stop()

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
    	left_motor_pin_1=20,
    	left_motor_pin_2=16,
    	right_motor_pin_1=19,
    	right_motor_pin_2=26):

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
