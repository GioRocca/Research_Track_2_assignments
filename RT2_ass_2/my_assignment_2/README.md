Assignment 1 Research Track I
=============================

Student: [Giovanni Rocca](https://github.com/GioRocca) (S4802954), Professor: [Carmine Tommaso Recchiuto](https://github.com/CarmineD8)
--------------------------------------------------------------------------------------------------------------------------------------

Goal of the simulation
----------------------

The goal for this simulation is to program a robot, making it able to reach a certain goal, decided by the user.
The robot and the goal are in an environment that contains some obstacles that the robot must avoid to reach the goal.

In this program, thanks to `node_a_client.py`, is possible to cancel the goal while the robot is moving by typing `s`, making the robot stop. After that the user has the possibility to define a new goal by following the instructions visualized in the Konsole window.

If the robot reaches the position of the goal, it is possible to define a new goal by typing `g` and following the instructions visualized in the Konsole window.

`node_a_publisher.py` takes the info relative to the position and velocity of the robot from the topic `/odom` and publish the message containing this info in the topic `/InfoRobot`.

`node_b.py` is a service node that, when called, prints the number of goals reached and cancelled;

`node_c.py` is a node that subscribes to the robot’s position and velocity and prints the distance of the robot from the target and the robot’s speed

Installing and running
----------------------

The simulation requires the installation of ROS, the `assignment_2_2022` package downloadable [clicking here](https://github.com/CarmineD8/assignment_2_2022), which provides an implementation of an action server that moves a robot in the environment by implementing the bug0 algorithm.

It also requires the installation of Konsole, by typing on the terminal: 

```bash
$ sudo apt-get install konsole
```

In order to make the .py files executable, type in the script directory:

```bash
$ chmod +x <name_of_file>
```

Once all is installed, simply run the simulation typing:

```bash
$ roslaunch my_assignment_2 assignment2.launch
```

### Flowchart ###

![Flowchart of node_a_client](/my_assignment_2/images/node_a_client_flowchart.PNG "Flowchart of node_a_client")

![Flowchart of node_a_publisher](/my_assignment_2/images/node_a_publisher_flowchart.PNG "Flowchart of node_a_publisher")



### Possible Improvements ###

Some possible improvements for this kind of robot can be, for example:

* Project the robot to scan the surrounding area in order to find the fastest path to reach the goal;

* Project the robot to be more safe, the robot could be designed to avoid collisions with obstacles, using collision sensors or some techniques;

* In general the possible improvements for this kind of robot can be try to make it more precise, reliable, fast and safe.
