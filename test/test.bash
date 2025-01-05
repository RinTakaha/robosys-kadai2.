#!/bin/bash

cd ~/ros2_ws
colcon build
source install/setup.bash

echo "Starting usage_tracker_node..."
ros2 run usage_tracker usage_tracker_node &
NODE_PID=$!

sleep 2

echo "Publishing start message..."
ros2 topic pub --once /start_time std_msgs/String "data: 'start'"

echo "Waiting for 10 seconds..."
sleep 10

echo "Publishing stop message..."
ros2 topic pub --once /stop_time std_msgs/String "data: 'stop'"

echo "Test completed!"
