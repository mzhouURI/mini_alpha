
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

from launch.substitutions import LaunchConfiguration

from launch.actions import DeclareLaunchArgument
from launch.substitutions import PythonExpression
from launch.actions import TimerAction

def generate_launch_description():
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'
    delay = LaunchConfiguration('delay')


    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config'
        )

    
    localization_param_file = os.path.join(robot_param_path, 'localization.yaml') 
    node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        namespace=robot_name,
        # output='screen',
        parameters=[localization_param_file],
    )


    return LaunchDescription([
        TimerAction(
            period=PythonExpression([delay]),
            actions=[node]
        ),
])
