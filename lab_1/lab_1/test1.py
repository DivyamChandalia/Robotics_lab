#!/usr/bin/env python3

import rclpy
import rclpy.node as node

def main(args = None):
    rclpy.init(args=args)
    node1 = node.Node("test")
    node1.get_logger().info("Hello World!")
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
