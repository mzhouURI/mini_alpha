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

    
    power_moinitor_param = os.path.join(
        get_package_share_directory(robot_bringup),
        'config',
        'power_monitor.yaml'
    )
    
    node = Node(
        package='power_monitor',
        executable='power_monitor_node',
        name='power_monitor_node',
        namespace=robot_name,
        output='screen',
        parameters=[power_moinitor_param]  
    )
    return LaunchDescription([
        TimerAction(
            period=PythonExpression([delay]),
            actions=[node]
        ),
    ])