import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Servo pin
SERVO_PIN = 12

# Setup servo pin as output
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize PWM on the servo pin at 50Hz frequency
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz (20ms period)
servo.start(7.5)  # Start at neutral position (1.5ms pulse width)

# Function to set servo angle based on duty cycle
def set_servo_angle(angle):
    duty = (angle / 18.0) + 2.5  # Convert angle to duty cycle
    servo.ChangeDutyCycle(duty)

# Function to calibrate the servo
def calibrate_servo():
    print("Calibrating servo...")

    # Move to 0 degrees
    print("Moving to 0 degrees")
    set_servo_angle(0)
    time.sleep(1)

    # Move to 90 degrees (neutral)
    print("Moving to 90 degrees (neutral)")
    set_servo_angle(90)
    time.sleep(1)

    # Move to 180 degrees
    print("Moving to 180 degrees")
    set_servo_angle(180)
    time.sleep(1)

    print("Servo calibration complete.")

try:
    calibrate_servo()

finally:
    servo.stop()
    GPIO.cleanup()
