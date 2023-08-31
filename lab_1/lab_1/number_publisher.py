#!/usr/bin/env python3

import rclpy
import rclpy.node as node
from std_msgs.msg import Int32

class NumberPublisher(node.Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.get_logger().info("Number Publisher has been started")
        self.create_timer(1/1,self.timer_call)
        self.obj_pub = self.create_publisher(Int32,"number",10)
        self.counter = 0

    def timer_call(self):
        msg = Int32()
        msg.data = self.counter
        self.obj_pub.publish(msg)
        self.get_logger().info(str(self.counter))
        self.counter += 1

def main(args = None):
    rclpy.init(args = args)
    node1 = NumberPublisher()
    rclpy.spin(node1)
    rclpy.shutdown()
