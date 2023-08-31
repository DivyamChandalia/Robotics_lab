#!/usr/bin/env python3

import rclpy
import rclpy.node as node
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleController(node.Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Turtle Controller has been started")
        self.obj_pub = self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.obj_sub = self.create_subscription(Pose,"turtle1/pose",self.sub_call,10)
        
        self.x = 3.0
        self.y = 8.0
    
    #make a proportioanl controller to go to a location x,y
    def sub_call(self,msg):
        distance = ((self.x - msg.x)**2 + (self.y - msg.y)**2)**0.5
        
        angle_to_goal = math.atan2(self.y - msg.y, self.x - msg.x)
        twist_msg = Twist()
        if distance > 0.2:
            
            twist_msg.linear.x = 2*distance
            twist_msg.angular.z = 6*(angle_to_goal - msg.theta)
        else:
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = 0.0
        self.obj_pub.publish(twist_msg)
        self.get_logger().info("Distance: " + str(distance) + " Angle: " + str(angle_to_goal - msg.theta))
        

def main(args = None):
    rclpy.init(args = args)
    node1 = TurtleController()
    rclpy.spin(node1)
    rclpy.shutdown()