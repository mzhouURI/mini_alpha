import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import TimerAction

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'
    delay = LaunchConfiguration('delay')

    presure_parameters = os.path.join(
        get_package_share_directory(robot_bringup),
        'config',
        'bluerobotics_bar30.yaml'
    )
    node = Node(
        package='bluerobotics_pressure',
        executable='bluerobotics_pressure_node',
        name='bluerobotics_pressure_node',
        namespace=robot_name,
        output='screen',
        parameters=[presure_parameters]    
    )
    return LaunchDescription([
        TimerAction(
            period=PythonExpression([delay]),
            actions=[node]
        ),
    ])
