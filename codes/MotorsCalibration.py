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
delay_us = 1000  # A reasonable delay for visible movement

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

def move_forward(steps=200):
    GPIO.output(dir_pin_left, GPIO.HIGH)  # Forward for left motor
    GPIO.output(dir_pin_right, GPIO.LOW)  # Forward for right motor
    for _ in range(steps):
        GPIO.output(step_pin_left, GPIO.HIGH)
        GPIO.output(step_pin_right, GPIO.HIGH)
        time.sleep(delay_us / 1000000.0)
        GPIO.output(step_pin_left, GPIO.LOW)
        GPIO.output(step_pin_right, GPIO.LOW)
        time.sleep(delay_us / 1000000.0)

def move_backward(steps=200):
    GPIO.output(dir_pin_left, GPIO.LOW)  # Reverse for left motor
    GPIO.output(dir_pin_right, GPIO.HIGH)  # Reverse for right motor
    for _ in range(steps):
        GPIO.output(step_pin_left, GPIO.HIGH)
        GPIO.output(step_pin_right, GPIO.HIGH)
        time.sleep(delay_us / 1000000.0)
        GPIO.output(step_pin_left, GPIO.LOW)
        GPIO.output(step_pin_right, GPIO.LOW)
        time.sleep(delay_us / 1000000.0)

def cleanup():
    GPIO.output(enable_pin_left, GPIO.HIGH)
    GPIO.output(enable_pin_right, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup_motors()
        print("Moving forward...")
        move_forward()  # Move forward to test motor direction
        time.sleep(1)
        print("Moving backward...")
        move_backward()  # Move backward to test motor direction
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
