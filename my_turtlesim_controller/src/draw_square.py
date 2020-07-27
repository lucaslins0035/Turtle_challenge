#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def publisher():
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(2)
    msg = Twist()
    counter = 0
    l = 5; a = 3.15
    while not rospy.is_shutdown():
        if counter == 0:
            msg.linear.x = l
            msg.angular.z = 0
            rospy.loginfo("FORWARD")
            pub.publish(msg)
            counter += 1
        elif counter == 1:
            msg.linear.x = 0
            msg.angular.z = a
            rospy.loginfo("TURN_RIGHT")
            pub.publish(msg)
            counter = 0
        rate.sleep()

if __name__ == "__main__":
    rospy.init_node("controller")
    publisher()
