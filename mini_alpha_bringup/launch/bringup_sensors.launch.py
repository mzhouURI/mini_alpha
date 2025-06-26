import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'

    parameters_file = os.path.join(get_package_share_directory(robot_bringup), 'config', 'xsens.yaml')

    return LaunchDescription([
        Node(
            package='xsens_mti_ros2_driver',
            namespace=robot_name,
            executable='xsens_mti_node',
            name='xsens_mti_node',
            prefix=['stdbuf -o L'],
            output="screen",
            parameters=[parameters_file],
            emulate_tty=True

        )
       
    ])