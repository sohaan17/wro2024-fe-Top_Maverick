Circuit Connections

Motors + servos - Arduino Uno (Output devices)

Cameras + Sensors -> Raspberry Pi

Logic for the code


If the bot sees a red pillar, go to the right lane.
If the bot sees a green pillar, go to the left lane.
If the bot sees the green green traffic sign , the bot will continue in the same direction.
If the bot sees the red traffic sign, the bot will make a u-turn and move in the opposite direction.
The bot will slow down at a distance of 20cm from the pillar and change the lanes.
After 3 laps the bot will find the 2 walls and parallel park itself

STRATEGY ->
Locate the nearest pillar on the basis of the camera's FOV
Move the long range ultrasonic to the pillar and get its distance
Drive towards the pillar.
Turn to the suitable direction at the suitable distance.
Move on to detecting the next obstacle.
On a turn, use the colour sensor or camera to detect lines and turn accordingly.
To keep a track of the laps, use the colour sensor.
