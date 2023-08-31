#!/usr/bin/env python3

import rclpy
import rclpy.node as node
import math

#make a client to call a service
from example_interfaces.srv import AddTwoInts

class ClientServer(node.Node):
    def __init__(self):
        super().__init__("client_server")
        self.get_logger().info("Client Server has been started")
        self.obj_client = self.create_client(AddTwoInts,"add_ints")
        while self.obj_client.wait_for_service(0.25) == False:
            self.get_logger().warn("Waiting for server")
        self.obj_req = AddTwoInts.Request()
        self.obj_req.a = 3
        self.obj_req.b = 4
        self.obj_future = self.obj_client.call_async(self.obj_req)
        rclpy.spin_until_future_complete(self,self.obj_future)
        
        try:
            self.obj_response = self.obj_future.result()
            self.get_logger().info(str(self.obj_req.a) + " + " + str(self.obj_req.b) + " = " + str(self.obj_response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

def main(args = None):
    rclpy.init(args = args)
    node1 = ClientServer()
    rclpy.spin(node1)
    rclpy.shutdown()

