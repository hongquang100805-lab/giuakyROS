import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
class EncoderReader(Node):
    def __init__(self):
        super().__init__('encoder_reader_node')
        # Tạo một Subscriber để nghe ngóng topic /mobile_base_controller/odom
        self.subscription = self.create_subscription(
            Odometry,
            '/mobile_base_controller/odom',
            self.odom_callback,
            10)     
        self.get_logger().info("Đang lắng nghe dữ liệu Encoder (Odometry)...")
        self.count = 0
    def odom_callback(self, msg):
        # Bộ đếm để giảm tốc độ in ra màn hình (chỉ in 1 lần sau mỗi 10 tin nhắn)
        # Vì Encoder gửi dữ liệu rất nhanh (khoảng 50 lần/giây)
        self.count += 1
        if self.count % 10 != 0:
            return
        # 1. Trích xuất Vị trí (X, Y)
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        
        # 2. Trích xuất Vận tốc tiến (v) và Vận tốc xoay (w)
        v = msg.twist.twist.linear.x
        w = msg.twist.twist.angular.z
        # 3. In ra Terminal (làm tròn 3 chữ số thập phân cho gọn)
        self.get_logger().info(
f' Vị trí: X={x: .3f}m, Y={y: .3f}m  |   Vận tốc: {v: .3f}m/s, Xoay: {w: .3f}rad/s'
        )
def main(args=None):
    rclpy.init(args=args)
    node = EncoderReader()
    try:
        rclpy.spin(node) # Vòng lặp vô tận để liên tục nhận dữ liệu
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()