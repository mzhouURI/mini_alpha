import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    arg_robot_name = 'mini_alpha'
    robot_bringup = arg_robot_name + '_bringup'


    foxglove = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('foxglove_bridge'),
                'launch/foxglove_bridge_launch.xml')),
        launch_arguments={
            'namespace': arg_robot_name,
            'delay': '1.0'
        }.items()
    )

    xsens = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(robot_bringup), 
                'launch','include','xsens.launch.py')),
        launch_arguments = {
            'arg_robot_name': arg_robot_name,
            'delay': '2.0'
            }.items()  
    )

    pressure = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(robot_bringup), 
                'launch','include','pressure_sensor.launch.py')),
        launch_arguments = {
            'arg_robot_name': arg_robot_name,
            'delay': '4.0'
            }.items()  
    )

    power = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(robot_bringup), 
                'launch','include','power_monitor.launch.py')),
        launch_arguments = {
            'arg_robot_name': arg_robot_name,
            'delay': '6.0'
            }.items()  
    )

    camera = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(robot_bringup), 
                'launch','include','camera.launch.py')),
        launch_arguments = {
            'arg_robot_name': arg_robot_name,
            'delay': '10.0'
            }.items()  
    )

    return LaunchDescription([
        foxglove,
        xsens,
        pressure,
        power,
        # camera
    ])