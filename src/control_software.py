from motor_control import MotorController
from sensor_interface import SensorInterface
import time

# Initialize motor and sensor controllers
motor_controller = MotorController(left_step_pin=19, left_dir_pin=16,
                                   right_step_pin=20, right_dir_pin=21)

sensor_interface = SensorInterface()

def main():
    try:
        print("Starting vehicle control software...")

        # Start motors at 60 RPM, gradually increasing to 120 RPM over 5 seconds
        motor_controller.accelerate_motors(60, 120, 5)
        
        while True:
            # Example: Get sensor data
            front_distance = sensor_interface.read_ultrasonic("front")
            left_distance = sensor_interface.read_ultrasonic("left")
            right_distance = sensor_interface.read_ultrasonic("right")
            
            print(f"Front: {front_distance} cm, Left: {left_distance} cm, Right: {right_distance} cm")

            # Example: Adjust motor behavior based on sensor data
            if front_distance < 30:
                print("Obstacle ahead! Stopping motors.")
                motor_controller.stop_motors()
            else:
                motor_controller.run_motors_at_rpm(120)
                
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("Stopping vehicle.")
        motor_controller.stop_motors()

if __name__ == "__main__":
    main()
