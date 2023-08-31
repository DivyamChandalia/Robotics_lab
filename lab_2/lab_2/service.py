#!/usr/bin/env python3

import rclpy
import rclpy.node as node
import math

#make a service to add 2 ints
from example_interfaces.srv import AddTwoInts

class ServiceServer(node.Node):
    def __init__(self):
        super().__init__("service_server")
        self.get_logger().info("Service Server has been started")
        self.obj_srv = self.create_service(AddTwoInts,"add_ints",self.srv_call)
    
    def srv_call(self,request,response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
        return response
    
def main(args = None):
    rclpy.init(args = args)
    node1 = ServiceServer()
    rclpy.spin(node1)
    rclpy.shutdown()