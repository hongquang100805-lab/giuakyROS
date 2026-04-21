cmake_minimum_required(VERSION 3.8)
project(urdf1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 1. Tìm các gói phụ thuộc
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)
find_package(gazebo_ros REQUIRED)

# 2. Lệnh Install: CẬP NHẬT ĐẦY ĐỦ 6 THƯ MỤC
install(
  DIRECTORY 
    launch 
    urdf 
    meshes 
    rviz 
    config   # Chứa file my_controllers.yaml
    scripts  # Chứa file super_teleop.py
  DESTINATION share/${PROJECT_NAME}
)

# 3. Kết thúc
ament_package()