#! /usr/bin/env python

import rospy
import actionlib
import assignment_2_2022.msg
from my_assignment_2.srv import Counter, CounterResponse

"""
..module:: node_b
	:platform: Unix
	:synopsis: This module contains the service node that counts the number of goals reached and the number of goals canceled.
    
..moduleauthor:: Giovanni Rocca

ROS node to count the number of goals reached and the number of goals canceled

Service:
	/numberGoals
    
Subscriber:
	/reaching_goal/result
    
"""

# counter variables
n_canceled = 0
n_reached = 0 

# counter function

def counterfunction(info):
	"""This function counts the number of goals reached and the number of goals canceled

	Args:
		info (PlanningActionResult): information about the goal

	"""
	global n_canceled, n_reached
	
	# if info.status.status = 2 the goal has been canceled
	if info.status.status == 2:
		n_canceled = n_canceled + 1
		
	# if info.status.status = 3 the goal has been reached
	elif info.status.status == 3:
		n_reached = n_reached + 1


def count(request):
	"""This function returns the number of goals reached and the number of goals canceled

	Args:
		request (CounterRequest): request to the service

	Returns:
		CounterResponse: response of the service
	"""
	global n_canceled, n_reached
	
	return CounterResponse(n_canceled, n_reached)

def main():
	"""This function initializes the node and creates the service
	
	"""

	# initialize the node
	rospy.init_node("node_b.py")
	
	# create the service 
	srv = rospy.Service("numberGoals", Counter, count)
	
	action = rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, counterfunction)

	rospy.spin()

if __name__ == '__main__':
	""" This is the main function
	
	"""
	main()
