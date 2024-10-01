import RPi.GPIO as GPIO
import time

step_pin_left = 19
dir_pin_left = 16
step_pin_right = 20
dir_pin_right = 21
enable_pin_left = 22
enable_pin_right = 27

steps_per_rev = 200
microstepping = 16
steps_per_full_rev = steps_per_rev * microstepping
target_rpm = 120
target_step_rate = (target_rpm * steps_per_full_rev) / 60
target_delay_us = 1000000 / target_step_rate

def setup_motors():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(step_pin_left, GPIO.OUT)
    GPIO.setup(dir_pin_left, GPIO.OUT)
    GPIO.setup(step_pin_right, GPIO.OUT)
    GPIO.setup(dir_pin_right, GPIO.OUT)
    GPIO.setup(enable_pin_left, GPIO.OUT)
    GPIO.setup(enable_pin_right, GPIO.OUT)
    GPIO.output(enable_pin_left, GPIO.LOW)
    GPIO.output(enable_pin_right, GPIO.LOW)
    GPIO.output(dir_pin_left, GPIO.HIGH)
    GPIO.output(dir_pin_right, GPIO.LOW)

def move_forward(duration=2):
    delayUs = target_delay_us
    end_time = time.time() + duration
    while time.time() < end_time:
        GPIO.output(step_pin_left, GPIO.HIGH)
        GPIO.output(step_pin_right, GPIO.HIGH)
        time.sleep(delayUs / 1000000.0)
        GPIO.output(step_pin_left, GPIO.LOW)
        GPIO.output(step_pin_right, GPIO.LOW)
        time.sleep(delayUs / 1000000.0)

def cleanup():
    GPIO.output(enable_pin_left, GPIO.HIGH)
    GPIO.output(enable_pin_right, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup_motors()
        move_forward()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
