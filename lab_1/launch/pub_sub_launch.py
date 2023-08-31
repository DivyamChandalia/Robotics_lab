#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab_1',
            executable='publisher',
            name='publisher'
        ),
        Node(
            package='lab_1',
            executable='subscriber',
            name='subscriber'
        )
    ])


