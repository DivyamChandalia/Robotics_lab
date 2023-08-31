import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import math
import random

class TurtleSpawner(Node):
    def __init__(self):
        super().__init__('spawn_turtle_node')
        self.service_client = self.create_client(Spawn, 'spawn')

        while not self.service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

        self.spawn_request = Spawn.Request()
        self.spawn_request.name = "turtle_kill"  # Replace with your desired turtle name

        # Modify this section to set random spawn coordinates
        self.spawn_request.x = random.random()*10  # Replace with your random x-coordinate
        self.spawn_request.y = random.random()*10  # Replace with your random y-coordinate
        self.spawn_request.theta = (random.random()*math.pi*2) - math.pi   # Replace with your random theta value
        self.spawn_turtle()

    def spawn_turtle(self):
        future = self.service_client.call_async(self.spawn_request)
        rclpy.spin_until_future_complete(self, future, timeout_sec=1.0)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner()
    # rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
