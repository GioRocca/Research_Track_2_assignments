#! /usr/bin/env python

import rospy
import math
from my_assignment_2.msg import Info
from my_assignment_2.msg import PositionVelocity

dist_vel = PositionVelocity()

# create a function to compute the distance and the speed
def compute_position_speed(info):

	global dist_vel
	
	# retrieve the goal position
	goal_pos_x = rospy.get_param("des_pos_x")
	goal_pos_y = rospy.get_param("des_pos_y")
	
	# Compute the distance between the robot and the goal position 
	dist_vel.distance = math.sqrt(pow(goal_pos_x - info.x, 2) + pow(goal_pos_y - info.y, 2))
	
	# Compute the velocity
	dist_vel.velocity = math.sqrt(pow(info.vel_x, 2) + pow(info.vel_y, 2))
	

def main():

	global dist_vel
	
	# initialize the node
	rospy.init_node("node_c.py")

	publisher = rospy.Publisher("/PosVel", PositionVelocity, queue_size = 10)
	
	rospy.Subscriber("/InfoRobot", Info, compute_position_speed)
	
	# set the rate at which the distance and speed are printed (info are every 2 seconds in this case)
	rate = rospy.Rate(0.5)
	
	# create an infinite loop to print the informations
	while True:
	
		publisher.publish(dist_vel)
		rate.sleep() 


if __name__ == '__main__':
	main()
