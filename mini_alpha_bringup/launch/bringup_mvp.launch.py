import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
import time

from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():
    arg_robot_name = 'mini_alpha'
    robot_bringup = arg_robot_name + '_bringup'


    #description URDF
    description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','description.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )

    # # robot localization
    localization = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','localization.launch.py')]),
        launch_arguments = {
            'arg_robot_name': arg_robot_name,
            'delay': '2.0'
            }.items()  
    )

    #mvp_control
    mvp_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','mvp_control.launch.py')]),
        launch_arguments = {
            'arg_robot_name': arg_robot_name,
            'delay': '5.0'
            }.items()  
    )

     #mvp_mission
    mvp_mission = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','mvp_mission.launch.py')]),
        launch_arguments = {
            'arg_robot_name': arg_robot_name,
            'delay': '10.0'
            }.items()  
    )


    return LaunchDescription([
        description,
        localization,
        mvp_control,
        mvp_mission,
    ])
