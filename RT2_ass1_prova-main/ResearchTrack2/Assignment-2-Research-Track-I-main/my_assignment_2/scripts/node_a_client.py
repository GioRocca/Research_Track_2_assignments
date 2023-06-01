#! /usr/bin/env python

import rospy
import assignment_2_2022.msg
import actionlib

"""
..module:: node_a_client
	:platform: Unix
	:synopsis: This module contains the client node that allows the user to define a goal and send it to the server node.

..moduleauthor:: Giovanni Rocca

ROS node to define a goal and send it to the server node

Action client:
	/reaching_goal

"""

# create a function that returns if the string passed as input is composed only by numbers or not
def is_number(string):
	"""This function returns if the string passed as input is composed only by numbers or not
	
	Args:
		string (String): string to check
	
	Returns:
		boolean: True if the string is composed only by numbers, False otherwise
	"""
	return string.isdigit()

# create a function to define a goal
def define_goal():
	"""This function allows the user to define a goal
	
	Returns:
		PlanningGoal: goal defined by the user
	"""

	print("Insert a goal")	

	while True:
		
		# get the x value from the user
		x = input("Enter the x value: ")
		
		# check if x is a number 
		if is_number(x):
			x = float(x)
			break
		
		else: 
			print("Invalid input, please insert only numbers\n ")
		
	while True:
		
		# get the y value from the user
		y = input("Enter the y value: ")
		
		# check if y is a number 
		if is_number(y):
			y = float(y)
			break
			
		else: 
			print("Invalid input, insert only numbers\n ")

	# Create a goal 
	new_goal = assignment_2_2022.msg.PlanningGoal()

	new_goal.target_pose.pose.position.x = x
	new_goal.target_pose.pose.position.y = y

	return new_goal

def main():
	"""This function initializes the node and creates a client that allows the user to define a goal and send it to the server node
	"""
	
	# initialize the node
	rospy.init_node("node_a_client.py")

	client = actionlib.SimpleActionClient("/reaching_goal", assignment_2_2022.msg.PlanningAction)

	client.wait_for_server()

	client.send_goal(define_goal())

	print("To stop the robot and define a new goal press s, while if the previous goal has been reached and you want to insert another one press g\n")

	# create an infinite loop that is listening for the user, who can stop the robot or insert a new goal
	while True:
		
		stop = input()	
		
		# Check if the action has not already succeeded and s is pressed
		if stop == "s" and client.get_state() != actionlib.GoalStatus.SUCCEEDED:
			
			# cancel the goal
			client.cancel_goal()
			
			# define a new goal
			client.send_goal(define_goal())
		
		# Check if the action has already succeeded and s is pressed
		elif stop == "s" and client.get_state() == actionlib.GoalStatus.SUCCEEDED:
			
			print ("You can't cancel the goal because it has alreay been reached ")
			
		# Check if the action has already succeeded and g is pressed
		elif stop == "g" and client.get_state() == actionlib.GoalStatus.SUCCEEDED:
		
			# define a new goal
			client.send_goal(define_goal())
		
		else: 
			
			print("Invalid key pressed\n ")			

if __name__ == '__main__':
	
	"""This is the main function that calls the function main()
	"""
	main()	

