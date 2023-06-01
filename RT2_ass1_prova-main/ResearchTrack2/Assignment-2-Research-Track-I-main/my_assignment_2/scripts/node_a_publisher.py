#! /usr/bin/env python

import rospy

from nav_msgs.msg import Odometry
from my_assignment_2.msg import Info

"""
..module:: node_a_publisher
	:platform: Unix
	:synopsis: This module contains the publisher node that publishes the robot's position and velocity.
    
..moduleauthor:: Giovanni Rocca

ROS node to publish the robot's position and velocity

Publisher:
	/InfoRobot
    
""" 

# publisher for the information about the robot's position and velocity
# The custom message Info contains the fields x,y (corresponding to the position) and the fields vel_x, vel_y (for the velocities)
publisher = rospy.Publisher("/InfoRobot", Info, queue_size=10) 

def robot_info_callback(info):

	"""This function publishes the robot's position and velocity

	Args:
		info (Odometry): information about the robot's position and velocity

	"""
    
	# Define the variable robot_info as the same type of the custom message
	# Fill all the fields of robot_info with the informations of the robot 

	robot_info = Info()
	  
	robot_info.x = info.pose.pose.position.x
	robot_info.y = info.pose.pose.position.y
	robot_info.vel_x = info.twist.twist.linear.x
	robot_info.vel_y = info.twist.twist.linear.y
	publisher.publish(robot_info)

def main():
	"""This function initializes the node and subscribes to the topic /odom.

	"""

	# initialize the node
	rospy.init_node('node_a_publisher.py')
	rospy.Subscriber("/odom", Odometry, robot_info_callback)
	rospy.spin()

if __name__ == '__main__':
	"""This is the main function that calls the function main()
	"""
	main()

