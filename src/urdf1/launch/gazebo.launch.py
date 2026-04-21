import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # 1. Khai báo tên package và các đường dẫn file
    package_name = 'urdf1'
    
    # SỬA TÊN FILE TẠI ĐÂY: đổi robot.urdf thành urdf1.urdf
    path_to_urdf = os.path.join(get_package_share_directory(package_name), 'urdf', 'urdf1.urdf')
    
    # --- ĐOẠN MỚI THÊM: Đường dẫn đến file config RViz2 ---
    rviz_config_file = os.path.join(get_package_share_directory(package_name), 'config', 'my_robot.rviz')
    
    # Xử lý file URDF qua xacro (để load các file mesh/định dạng robot)
    robot_description_raw = xacro.process_file(path_to_urdf).toxml()

    # 2. Node Robot State Publisher
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_raw, 
            'use_sim_time': True
        }]
    )

    # 3. Khởi chạy Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    )

    # 4. Node Spawn Entity (Thả robot vào Gazebo)
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'quang_robot'],
        output='screen'
    )

    # 5. Khai báo các Controller Spawner
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
    )

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["mobile_base_controller"],
    )

    arm_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller"],
    )

    # --- ĐOẠN MỚI THÊM: Node chạy RViz2 ---
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': True}]
    )

    # 6. Trình tự khởi chạy: Chờ 3 giây sau khi spawn robot mới bật controller
    return LaunchDescription([
        node_robot_state_publisher,
        gazebo,
        spawn_entity,
        rviz_node,  # <--- ĐÃ THÊM RVIZ VÀO DANH SÁCH KHỞI CHẠY
        
        TimerAction(
            period=3.0,
            actions=[
                joint_state_broadcaster_spawner,
                diff_drive_spawner,
                arm_controller_spawner
            ]
        )
    ])