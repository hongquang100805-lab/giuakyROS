# Dự án ROS 2 – Xe 4 bánh Omni + Tay máy (2DOF)

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange)

---

##  Clone & Quick Start

```bash
git clone https://github.com/hongquang100805-lab/giuakyROS.git
cd giuakyROS
colcon build
source install/setup.bash
```
---



## Hiển thị mô phỏng (Gazebo + RViz)

```bash
ros2 launch urdf1 gazebo.launch.py
```

---

## Điều khiển robot Omni (bằng bàn phím)

### Bước 1: Mở terminal mới

### Bước 2:

```bash
source install/setup.bash
```

### Bước 3:

```bash
python3 src/urdf1/scripts/super_teleop.py
```

---

##  Điều khiển tay máy (2DOF) den vi tri mong muon 

### Bước 1: Mở terminal mới

### Bước 2:

```bash
source install/setup.bash
```

### Bước 3:

```bash
python3 src/urdf1/scripts/move_arm.py
```


---

## Hiển thị dữ liệu cảm biến

### Bước 1: Mở terminal mới

### Bước 2:

```bash
source install/setup.bash
```

### 🔹 Encoder

```bash
python3 src/urdf1/scripts/read_encoder.py
```

### 🔹 IMU

```bash
python3 src/urdf1/scripts/read_imu.py
```

---

