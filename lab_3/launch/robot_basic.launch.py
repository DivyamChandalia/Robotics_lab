from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    urdf = "/home/divyamc/divyam_ws/src/lab_3/urdf/robot_scratch.urdf"
    robot_node = Node(
        package= "robot_state_publisher",
        executable= "robot_state_publisher",
        name= "robot_state_publisher",
        output= "screen",
        arguments= [urdf]
    )
    joint_node = Node(
        package= "joint_state_publisher_gui",
        executable= "joint_state_publisher_gui",
        name= "joint_state_publisher",
        output= "screen",
        arguments= [urdf]
    )
    rviz_node = Node(
        package= "rviz2",
        executable= "rviz2",
        name= "rviz2",
        output= "screen",
    )
    ld.add_action(robot_node)
    ld.add_action(joint_node)
    ld.add_action(rviz_node)
    return ld