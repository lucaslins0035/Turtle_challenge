#!/usr/bin/env python

import rospy
from ds4_driver.msg import Status
from geometry_msgs.msg import Twist

def convert_to_cmd_vel(msg): 
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10) 
    resp = Twist()
    l = 3; a = 3
    resp.linear.x = msg.axis_left_y*l
    resp.angular.z = msg.axis_right_x*a
    pub.publish(resp)

def subscriber():   
    sub = rospy.Subscriber("/status",Status,convert_to_cmd_vel,queue_size=10)
    rospy.spin()
    

if __name__ == "__main__":
    rospy.init_node("ds4_converter")
    rospy.loginfo("""
    Use:
    Left_Stick to move;
    Right_Stick to turn;""")
    while not rospy.is_shutdown():
        subscriber()