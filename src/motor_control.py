import RPi.GPIO as GPIO
import time

class MotorController:
    def __init__(self, left_step_pin, left_dir_pin, right_step_pin, right_dir_pin):
        self.left_step_pin = left_step_pin
        self.left_dir_pin = left_dir_pin
        self.right_step_pin = right_step_pin
        self.right_dir_pin = right_dir_pin
        
        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_step_pin, GPIO.OUT)
        GPIO.setup(self.left_dir_pin, GPIO.OUT)
        GPIO.setup(self.right_step_pin, GPIO.OUT)
        GPIO.setup(self.right_dir_pin, GPIO.OUT)

        GPIO.output(self.left_dir_pin, GPIO.LOW)   # Left motor direction
        GPIO.output(self.right_dir_pin, GPIO.HIGH)  # Right motor direction

    def run_motors_at_rpm(self, rpm):
        step_rate = self.rpm_to_steps_per_second(rpm)
        self.control_motor_speed(step_rate, step_rate)
    
    def accelerate_motors(self, start_rpm, target_rpm, duration):
        step_rate_start = self.rpm_to_steps_per_second(start_rpm)
        step_rate_target = self.rpm_to_steps_per_second(target_rpm)
        steps = 50  # Incremental steps
        increment = (step_rate_target - step_rate_start) / steps
        for i in range(steps):
            current_step_rate = step_rate_start + i * increment
            self.control_motor_speed(current_step_rate, current_step_rate)
            time.sleep(duration / steps)
    
    def control_motor_speed(self, step_rate_left, step_rate_right):
        delay_left = 1.0 / step_rate_left
        delay_right = 1.0 / step_rate_right
        GPIO.output(self.left_step_pin, GPIO.HIGH)
        time.sleep(delay_left)
        GPIO.output(self.left_step_pin, GPIO.LOW)
        time.sleep(delay_left)
        GPIO.output(self.right_step_pin, GPIO.HIGH)
        time.sleep(delay_right)
        GPIO.output(self.right_step_pin, GPIO.LOW)
        time.sleep(delay_right)

    def stop_motors(self):
        GPIO.output(self.left_step_pin, GPIO.LOW)
        GPIO.output(self.right_step_pin, GPIO.LOW)

    def rpm_to_steps_per_second(self, rpm):
        steps_per_rev = 200
        microstepping = 16
        steps_per_full_rev = steps_per_rev * microstepping
        return (rpm * steps_per_full_rev) / 60

    def cleanup(self):
        GPIO.cleanup()
