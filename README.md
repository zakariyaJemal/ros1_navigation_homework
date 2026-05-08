# ROS1 Navigation Homework

## Project Description
This project was developed using ROS Noetic and TurtleBot3.  
The robot creates a map using SLAM and autonomously navigates through 5 different waypoint positions.

## Technologies Used
- ROS Noetic
- TurtleBot3
- Gazebo
- RViz
- Python

## Project Steps
1. Map creation using SLAM
2. Saving the generated map
3. Running the navigation stack
4. Defining 5 waypoint coordinates
5. Autonomous waypoint navigation using Python script

## Run Commands

### Start Gazebo
```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch

## Start Navigation
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/robtk_ws/src/my_robot_navigation/maps/map.yaml


##Run Waypoint Script
rosrun my_robot_navigation waypoint_nav.py

##Waypoint Format
(x, y, 0.0, 1.0)
