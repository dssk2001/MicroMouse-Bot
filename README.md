# MicroMouse-Bot
The famous Micro Mouse bot simulated in Gazebo.<br>

Installing ROS is Mandatory prior to this.<br>

For those who are intrested in simulating the bot create a catkin package and then in the src folder clone the repositories and  it's done.<br>
For launching the bot in Gazebo cd into your catkin ws and build it using catkin_make and source it. Then cd into src and using roslaunch launch it using "roslaunch bot_gazebo bot.launch".<br>
This will launch you bot into Gazebo.<br>

In a new terminal cd into your catkin ws and catkin_make and source it. Then cd into src and using rosrun launch the node as "rosrun bot_control move1.py".<br>
This will start moving your bot in the world.<br>
