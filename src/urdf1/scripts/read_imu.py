import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu  # Khai báo thư viện để đọc dữ liệu cảm biến

class ImuReader(Node):
    def __init__(self):
        super().__init__('imu_reader_node')
        # Tạo Subscriber nghe topic /imu/data
        self.subscription = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            10)
        self.get_logger().info("Đang lắng nghe dữ liệu IMU...")
        self.count = 0
    def imu_callback(self, msg):
        # Bộ đếm để giảm tốc độ in (chỉ in 1 lần sau mỗi 10 tin nhắn)
        self.count += 1
        if self.count % 10 != 0:
            return
        # 1. Trích xuất Gia tốc tuyến tính (Linear Acceleration) - Đo va chạm, tăng tốc
        accel_x = msg.linear_acceleration.x
        accel_y = msg.linear_acceleration.y
        accel_z = msg.linear_acceleration.z # Trục Z thường ~9.8 do trọng lực Trái Đất
        # 2. Trích xuất Vận tốc góc (Angular Velocity) - Đo tốc độ xoay
        gyro_z = msg.angular_velocity.z # Khi xe rẽ trái/phải trên mặt đất, trục Z sẽ thay đổi
        # 3. In ra Terminal
        self.get_logger().info(
f' Gia tốc (m/s²): X={accel_x: .2f}, Y={accel_y: .2f}, Z={accel_z: .2f}  |   Xoay: Z={gyro_z: .2f} rad/s'
        )
def main(args=None):
    rclpy.init(args=args)
    node = ImuReader()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()