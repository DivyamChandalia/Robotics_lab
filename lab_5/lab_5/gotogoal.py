import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math

class TrajectoryPublisher(Node):

    def __init__(self):
        super().__init__('trajectory_node')
        topic_ = "/joint_trajectory_controller/joint_trajectory"
        self.joints = ['base_arm1_joint', 'arm1_arm2_joint', 'arm2_arm3_joint']
        self.declare_parameter("x", 0.0)
        self.declare_parameter("z", 1.0)

        self.goal_x_ = self.get_parameter("x").value
        self.goal_z_ = self.get_parameter("z").value
        self.publisher_ = self.create_publisher(JointTrajectory, topic_, 10)
        self.timer_ = self.create_timer(1, self.timer_callback)
        self.goal_ = self.inverse_kinematics(self.goal_x_, self.goal_z_)

    def inverse_kinematics(self, x, z):
        L1 = 0.5
        L2 = 0.5
        L3 = 0.3
        # Calculate θ1 (angle at the base joint)
        theta1 = math.atan2(self.goal_x_, self.goal_z_)

        # Calculate θ3 (angle at the end-effector joint)
        D = (self.goal_z_ ** 2 + self.goal_x_ ** 2 - L1 ** 2 - L2 ** 2 - L3 ** 2) / (2 * L2 * L3)
        if -1 <= D <= 1:
            theta3 = math.atan2(-math.sqrt(1 - D**2), D)
        else:
            print("No valid solution exists for the given goal position.")
            return [0.0, 0.0, 0.0]


        # Calculate θ2 (angle at the second joint)
        K1 = L1 + L2 * math.cos(theta3)
        K2 = L2 * math.sin(theta3)
        theta2 = math.atan2(self.goal_x_, self.goal_z_) - math.atan2(K2, K1)

        return [theta1, theta2, theta3]

    def timer_callback(self):
        msg = JointTrajectory()
        msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = self.goal_
        point.time_from_start = Duration(sec=2)
        msg.points.append(point)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
