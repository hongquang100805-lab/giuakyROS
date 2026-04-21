# Dự án ROS 2 – Xe 4 bánh Omni + Tay máy (2DOF)

##  Các bước chạy package

### Bước 1: Di chuyển đến workspace

```bash
cd ~/ros2_ws
```

### Bước 2: Source môi trường

```bash
source install/setup.bash
```

---

## Hiển thị model trên Gazebo + RViz

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

## Điều khiển tay máy (2DOF)

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

##  Hiển thị thông số cảm biến

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

##  Ghi chú

* Đảm bảo đã `colcon build` trước khi chạy
* Kiểm tra package `urdf1` đã tồn tại trong workspace

---

