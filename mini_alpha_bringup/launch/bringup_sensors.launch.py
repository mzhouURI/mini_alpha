import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'

    xsens_parameters_file = os.path.join(
        get_package_share_directory(robot_bringup), 
        'config', 
        'xsens.yaml')

    presure_parameters = os.path.join(
        get_package_share_directory(robot_bringup),
        'config',
        'bluerobotics_bar30.yaml'
    )

    power_moinitor_param = os.path.join(
        get_package_share_directory(robot_bringup),
        'config',
        'power_monitor.yaml'
    )

    return LaunchDescription([
        Node(
            package='xsens_mti_ros2_driver',
            namespace=robot_name,
            executable='xsens_mti_node',
            name='xsens_mti_node',
            prefix=['stdbuf -o L'],
            output="screen",
            parameters=[xsens_parameters_file],
            emulate_tty=True
        ),
        Node(
            package='bluerobotics_pressure',
            executable='bluerobotics_pressure_node',
            name='bluerobotics_pressure_node',
            namespace=robot_name,
            output='screen',
            parameters=[presure_parameters]        
        ),

        Node(
            package='power_monitor',
            executable='power_monitor_node',
            name='power_monitor_node',
            namespace=robot_name,
            output='screen',
            parameters=[power_moinitor_param]        
        )

       
    ])