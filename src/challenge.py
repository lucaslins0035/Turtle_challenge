#!/usr/bin/env python

import rospy,math,sys
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Turtle():
    def __init__(self,name,max_linear,max_steer,target):
        self.max_steer = max_steer
        self.max_linear = max_linear
        self.target = target
        self.name = name
        self.pub = rospy.Publisher("/{}/cmd_vel".format(self.name),Twist,queue_size=10)    
    
    def subscriber(self):
        self.sub = rospy.Subscriber("/{}/pose".format(self.name),Pose,self.move)
        rospy.spin()

    def move(self,msg):
        dx = self.target[0]-msg.x; dy = self.target[1]-msg.y # Calculates vector_towards_target
        mov = Twist()
        if((dx**2+dy**2)**0.5<=0.1): #If arrived
            mov.linear.x = 0
            mov.angular.z = 0
            self.pub.publish(mov)
            rospy.loginfo("""
Arrived at:
    x: {}
    y: {}
theta: {}
            """.format(msg.x,msg.y,msg.theta))
            rospy.signal_shutdown("ARRIVED")
        else:
            dabs = (dx**2+dy**2)**0.5 #Calculate |vector_towards_target|
            self.desired = (dx/dabs,dy/dabs) #Assign as tuple
            steer_factor = (math.cos(msg.theta)*self.desired[1]-math.sin(msg.theta)*self.desired[0]) #Calculate steer factor based on the turtle theta angle and the vector_towards_target
            mov.linear.x = (1-abs(steer_factor))*self.max_linear #To lower the path, linear vel is small when angular vel is high
            mov.angular.z = steer_factor*self.max_steer
            self.pub.publish(mov)

if __name__ == "__main__":
    rospy.init_node("path_planning")
    if(len(sys.argv)==3): #Check arguments
        if(float(sys.argv[1])>=0 and float(sys.argv[1])<=11 and float(sys.argv[2])>=0 and float(sys.argv[2])<=11): #Check coordinates values
            t1 = Turtle("turtle1",2,4,(float(sys.argv[1]),float(sys.argv[2])))
            rospy.loginfo("Ready!")
            t1.subscriber()
        else: rospy.loginfo(" WARNING: 0 <= x,y <= 11")
    else:
        rospy.loginfo("Assign: x y (Destiny coordinates)")
    

    


