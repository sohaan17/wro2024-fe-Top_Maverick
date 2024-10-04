import time
import board
import adafruit_tcs34725

# Initialize the I2C bus and sensor
i2c = board.I2C()  # Use default I2C pins
sensor = adafruit_tcs34725.TCS34725(i2c)

# Enable light sensor
sensor.integration_time = 100  # Higher integration times give more stable readings
sensor.gain = 4  # Set gain to increase or decrease sensitivity

# Function to measure and return raw color data
def get_color_reading():
    color_data = sensor.color_raw
    return color_data

# Function to calibrate the sensor using known color samples
def calibrate_color_sensor():
    colors = {
        "white": [0, 0, 0],  # Will store average values for white
        "red": [0, 0, 0],    # For red sample
        "green": [0, 0, 0],  # For green sample
        "blue": [0, 0, 0]    # For blue sample
    }

    print("Starting color calibration...")

    for color_name in colors.keys():
        input(f"Place the {color_name} sample in front of the sensor and press Enter...")
        
        r_sum, g_sum, b_sum = 0, 0, 0
        num_samples = 10  # Take multiple samples for accuracy

        for _ in range(num_samples):
            r, g, b = get_color_reading()
            r_sum += r
            g_sum += g
            b_sum += b
            time.sleep(0.1)  # Wait between readings for sensor stability

        # Calculate average readings for this color
        colors[color_name] = [r_sum // num_samples, g_sum // num_samples, b_sum // num_samples]
        print(f"Average {color_name} RGB readings: {colors[color_name]}")

    print("Color sensor calibration complete.")
    print("Final Calibration Data: ", colors)

try:
    calibrate_color_sensor()

finally:
    print("Calibration finished.")
