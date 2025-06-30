import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction


def generate_launch_description():
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'
    joy_param = os.path.join(
        get_package_share_directory(robot_bringup),
        'config', 'tele_thruster.yaml'
        )
    
    return LaunchDescription([

    Node(
        package="joy_thruster_map",
        executable="joy_thruster_map",
        namespace=robot_name,
        name="surge_teleop",
        parameters=[joy_param],
        output='screen'   
        ),

    Node(
            package="joy",
            executable="joy_node",
            name="joy_node",
            namespace=robot_name,
            output="screen",
            parameters=[
                {'coalesce_interval': 10},
                {'autorepeat_rate': 0.0}
            ],
            remappings=[
                ('joy', 'mvp_helm/bhv_teleop/joy'),
            ]   
        ), 
    ])
        