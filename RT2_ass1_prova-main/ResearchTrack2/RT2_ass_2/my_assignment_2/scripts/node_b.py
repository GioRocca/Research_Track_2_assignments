#! /usr/bin/env python

import rospy
import actionlib
import assignment_2_2022.msg
from my_assignment_2.srv import Counter, CounterResponse


# counter variables
n_canceled = 0
n_reached = 0 

# counter function
def counterfunction(info):
	global n_canceled, n_reached
	
	# if info.status.status = 2 the goal has been canceled
	if info.status.status == 2:
		n_canceled = n_canceled + 1
		
	# if info.status.status = 3 the goal has been reached
	elif info.status.status == 3:
		n_reached = n_reached + 1
		 

def count(request):
	global n_canceled, n_reached
	
	return CounterResponse(n_canceled, n_reached)

def main():

	# initialize the node
	rospy.init_node("node_b.py")
	
	# create the service 
	srv = rospy.Service("numberGoals", Counter, count)
	
	action = rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, counterfunction)

	rospy.spin()
	
if __name__ == '__main__':
	main()
