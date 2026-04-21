import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # 1. Khai báo tên package và đường dẫn
    pkg_name = 'urdf1'
    pkg_path = os.path.join(get_package_share_directory(pkg_name))
    
    # Đảm bảo đường dẫn này đúng với file bạn xuất từ SolidWorks
    # Thường là thư mục urdf/ và tên file là robot.urdf hoặc urdf1.urdf
    path_to_urdf = os.path.join(pkg_path, 'urdf', 'urdf1.urdf') 

    # 2. Xử lý file URDF (dùng xacro để đọc cho chuẩn)
    robot_description_raw = xacro.process_file(path_to_urdf).toxml()

    # 3. Cấu hình các Node
    # Node 1: Robot State Publisher (Quản lý khung xương robot)
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}]
    )

    # Node 2: Joint State Publisher GUI (Tạo bảng điều khiển các khớp để bạn xoay thử)
    node_joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # Node 3: RViz2 (Giao diện hiển thị)
    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        node_robot_state_publisher,
        node_joint_state_publisher_gui,
        node_rviz
    ])