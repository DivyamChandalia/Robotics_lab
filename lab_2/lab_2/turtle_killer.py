#!/usr/bin/env python3

import rclpy
import rclpy.node as node
import math
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from geometry_msgs.msg import Twist

class TurtleKiller(node.Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.kill = self.create_subscription(Pose,"turtle_kill/pose",self.target,10)
        self.pose = self.create_subscription(Pose,"turtle1/pose",self.move,10)
        self.cmd_vel = self.create_publisher(Twist,"turtle1/cmd_vel",10)

        self.service_client = self.create_client(Kill, 'kill')

        self.x = None
        self.y = None
    
    def target(self,msg):
        self.x = msg.x
        self.y = msg.y

    def despawn_turtle(self):
        while not self.service_client.wait_for_service(timeout_sec=1.0):
            continue

        self.despawn_request = Kill.Request()
        self.despawn_request.name = 'turtle_kill'
        future = self.service_client.call_async(self.despawn_request)

    #make a proportioanl controller to go to a location x,y
    def move(self, msg):
        if self.x is None or self.y is None:
            return
        
        distance = ((self.x - msg.x)**2 + (self.y - msg.y)**2)**0.5
        
        angle_to_goal = math.atan2(self.y - msg.y, self.x - msg.x)
        twist_msg = Twist()
        
        if distance > 0.2:
            twist_msg.linear.x = 2 * distance
            
            # Calculate the difference between the current and goal angles
            angle_difference = angle_to_goal - msg.theta
            
            # Ensure that angle_difference is within the range of -π to π
            if angle_difference > math.pi:
                angle_difference -= 2 * math.pi
            elif angle_difference < -math.pi:
                angle_difference += 2 * math.pi
                
            twist_msg.angular.z = 6 * angle_difference
        else:
            self.x = None
            self.y = None
            self.despawn_turtle()
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = 0.0
        
        # Perform the necessary action with twist_msg (publishing, etc.)

        self.get_logger().info(f"distance: {distance}")
        self.get_logger().info(f"angle_to_goal: {angle_to_goal}")
        self.cmd_vel.publish(twist_msg)
        

def main(args = None):
    rclpy.init(args = args)
    node1 = TurtleKiller()
    rclpy.spin(node1)
    rclpy.shutdown()