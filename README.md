# Du an ROS 2- XE 4 banh Onmi with tay may(2DOF)
# Các bước để chạy được package:
Buoc 1. dung len : cd ~/ros2_ws

Buoc 2: source install/setup.bash

### * Hiển thị cung luc Model trên gazebo va RViz *

ros2 launch urdf1 gazebo.launch.py


### * Điều Khiển Robot Omni *

Điều khiển chuyển động banh xe va tay may bang ban phim của robot base (4 bánh omni).

python3 src/urdf1/scripts/super_teleop.py


### *Dieu khien Tay Robot (2 Khớp) den vi tri mong muon *

python3 src/urdf1/scripts/move_arm.py


### * Hien thi thong so cam bien*
1. thong so encorder:  python3 src/urdf1/scripts/read_encoder.py
2. thong so IMU : python3 src/urdf1/scripts/read_imu.py

