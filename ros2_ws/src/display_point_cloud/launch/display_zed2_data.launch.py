from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ZEDData',
            executable='zed2_data_acquisition',
            name='zed2_data_acquisition',
            output='screen'
        ),
        Node(
            package='display_point_cloud',
            executable='3d_point_input',
            name='point_cloud_display',
            output='screen'
        ),
    ])
