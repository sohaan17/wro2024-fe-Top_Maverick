# WRO 2024 - Vehicle Control Software

This repository contains the control software developed for the [WRO Future Engineers 2024 competition](https://www.worldrobotolympiad.org). The software controls the vehicle's movement, sensors, and motors to navigate through the competition tasks.

## Team Information
- **Team Name**: [Your Team Name]
- **Participants**: [List participant names]
- **Competition Category**: Future Engineers
- **Competition Year**: 2024

## Project Description

The software in this repository is responsible for controlling the vehicle’s motors, sensors, and decision-making algorithms as required by the competition rules. This includes:
- Controlling two motors with TMC2100 stepper drivers.
- Sensing obstacles and environmental features with ultrasonic and magnetometer sensors.
- Color detection using a TCS3200 color sensor.
- Implementing gradual acceleration and speed control logic.

## Getting Started

### Hardware Requirements
- Raspberry Pi 4 with Raspbian OS
- Two stepper motors (NEMA 17) controlled by TMC2100 stepper drivers
- Seed Studio Grove Ultrasonic sensor for distance measurement
- HW246 GY-271 magnetometer for orientation detection
- GY-31 TCS3200 color sensor module

### Software Requirements
- Python 3.x
- Required Python libraries:
  - `RPi.GPIO` for GPIO control
  - `time` for timing functions

### How to Set Up

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/WRO2024-Control-Software.git
