import RPi.GPIO as GPIO
import time

# Define GPIO pins for the ultrasonic sensor
TRIG_PIN = 23
ECHO_PIN = 24

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setup the pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Function to measure distance using the ultrasonic sensor
def measure_distance():
    # Ensure the trigger pin is low for a short delay
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.2)

    # Trigger the ultrasonic pulse
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10 microseconds pulse
    GPIO.output(TRIG_PIN, False)

    # Wait for the echo pin to go high
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    # Wait for the echo pin to go low
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calculate the duration of the echo pulse
    pulse_duration = pulse_end - pulse_start

    # Calculate distance in cm (speed of sound is ~34300 cm/s in air)
    distance = pulse_duration * 17150

    # Return the measured distance
    return distance

# Calibrate the sensor by taking multiple measurements at known distances
def calibrate_sensor():
    known_distances = [10, 20, 30, 40, 50]  # Known distances in cm
    sensor_readings = []

    for distance in known_distances:
        input(f"Place an object at {distance} cm and press Enter...")
        measurement = measure_distance()
        print(f"Measured distance: {measurement:.2f} cm")
        sensor_readings.append(measurement)

    print("Known distances: ", known_distances)
    print("Sensor readings: ", sensor_readings)

    # Optionally, calculate a scaling factor or correction for accuracy
    # Example: scaling_factor = sum(known_distances) / sum(sensor_readings)

try:
    calibrate_sensor()

finally:
    GPIO.cleanup()  # Clean up GPIO pins
