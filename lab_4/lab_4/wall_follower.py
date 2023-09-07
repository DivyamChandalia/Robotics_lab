#!/usr/bin/env python3

import rclpy
import rclpy.node as node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class BotController(node.Node):
    def __init__(self):
        super().__init__("bot_controller")
        self.get_logger().info("Wall Follower has been started")
        self.obj_pub = self.create_publisher(Twist,"/cmd_vel",10)
        self.obj_sub = self.create_subscription(LaserScan,"/gazebo_lidar/out",self.cmd_vel,10)
    
    #make a controller to stop if it goes too close to a wall else move forward
    def cmd_vel(self, laser):
        twist_msg = Twist()
        for laser in laser.ranges:
            if laser < 1:
                twist_msg.linear.x = 0.0
                twist_msg.angular.z = 0.0
                print("Too close to wall")
                break
            else:
                twist_msg.linear.x = 0.5
                twist_msg.angular.z = 0.0
        
        self.obj_pub.publish(twist_msg)
        
def main(args = None):
    rclpy.init(args = args)
    node1 = BotController()
    rclpy.spin(node1)
    rclpy.shutdown()