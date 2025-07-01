import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction
from launch.substitutions import PythonExpression

def generate_launch_description():
    """
    Launch file to run two instances of the dwe_camera_node for two cameras,
    with remappings to ensure topics are unique.
    """
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'

    delay = LaunchConfiguration('delay')
    
    # The package name is 'dwe_camera' as defined in setup.py
    robot_param_path = get_package_share_directory(robot_bringup)

    dual_camera_params_path = os.path.join(robot_param_path, 'config', 'dual_cameras.yaml')

    exploreHD_camera_node = Node(
        package='dwe_camera_driver',
        executable='camera_node',
        name='exploreHD_camera_node',
        namespace=robot_name,
        output='screen',
        parameters=[dual_camera_params_path],
        remappings=[
            ('image/compressed', 'exploreHD/image/compressed'),
            ('image_lowbw/compressed', 'exploreHD/image_lowbw/compressed'),
            ('camera_settings', 'exploreHD/camera_settings'),
        ]
    )

    usbpcb_camera_node = Node(
        package='dwe_camera_driver',
        executable='camera_node',
        name='usbpcb_camera_node',
        namespace=robot_name,
        output='screen',
        parameters=[dual_camera_params_path],
        remappings=[
            ('image/compressed', 'usbpcb/image/compressed'),
            ('image_lowbw/compressed', 'usbpcb/image_lowbw/compressed'),
            ('camera_settings', 'usbpcb/camera_settings'),
        ]
    )

    return LaunchDescription([
        TimerAction(
            period=PythonExpression([delay]),
            actions=[exploreHD_camera_node, usbpcb_camera_node]
        ),
        
    ])