#!/usr/bin/env python3

import rclpy
import rclpy.node as node
from std_msgs.msg import Int32

class NumberPublisher(node.Node):
    def __init__(self):
        super().__init__("number_counter")
        
        self.get_logger().info("Number Counter has been started")
        self.obj_pub = self.create_publisher(Int32,"number_count",10)
        self.counter = 0
        self.obj_sub = self.create_subscription(Int32,"number",self.sub_call,10)

    def sub_call(self,msg):
        self.counter += msg.data
        msg = Int32()
        msg.data = self.counter
        self.obj_pub.publish(msg)
        self.get_logger().info(str(self.counter))

def main(args = None):
    rclpy.init(args = args)
    node1 = NumberPublisher()
    rclpy.spin(node1)
    rclpy.shutdown()
