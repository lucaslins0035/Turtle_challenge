# TURTLE CHALLENGE

**Description:** This package provides a position controller for the turtlesim turtle

**Maintainer:** Lucas Lins Souza

**Dependencies:** `turtlesim` package

## Installation

Clone the repository into a catkin workspace, compile and source. 

## Usage:

Open the turtlesim_node: 
```
rosrun turtlesim turtlesim_node
```
Open the `challenge.py` file passing the 'x' and 'y' parameters that indicates the destination of the turtle:
```
rosrun turtle_challenge challenge.py 3.6 8.9
```
The turtle will reach the specified point with a max. error of 0.1. After it reaches the destination, the final position of the turtle is printed and the node is closed.

> Note: 0 <= x , y <= 11