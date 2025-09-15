'''
event_logger launch file
'''

import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Generate launch description for event_logger server

    Returns:
        LaunchDescription: The launch description for event_logger events listener
    """
    # create bridge composition
    event_logger = Node(
        package='event_logger',
        executable='event_logger_node',
        name='listener',
        output='screen',
        arguments=['--ros-args', '--log-level', 'info']
    )

    # return
    return LaunchDescription([
        event_logger
    ])
