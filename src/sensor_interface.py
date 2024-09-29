import RPi.GPIO as GPIO
import time

class SensorInterface:
    def __init__(self):
        self.front_trig = 17
        self.front_echo = 27
        self.left_trig = 23
        self.left_echo = 24
        self.right_trig = 22
        self.right_echo = 5
        self.setup_ultrasonic()

    def setup_ultrasonic(self):
        GPIO.setup(self.front_trig, GPIO.OUT)
        GPIO.setup(self.front_echo, GPIO.IN)
        GPIO.setup(self.left_trig, GPIO.OUT)
        GPIO.setup(self.left_echo, GPIO.IN)
        GPIO.setup(self.right_trig, GPIO.OUT)
        GPIO.setup(self.right_echo, GPIO.IN)

    def read_ultrasonic(self, sensor):
        if sensor == "front":
            trig, echo = self.front_trig, self.front_echo
        elif sensor == "left":
            trig, echo = self.left_trig, self.left_echo
        elif sensor == "right":
            trig, echo = self.right_trig, self.right_echo
        else:
            return None

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        start_time = time.time()
        stop_time = time.time()
        while GPIO.input(echo) == 0:
            start_time = time.time()
        while GPIO.input(echo) == 1:
            stop_time = time.time()
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2
        return distance
