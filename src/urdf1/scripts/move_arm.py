import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
class ArmControllerNode(Node):
    def __init__(self):
        super().__init__('arm_controller_node')
        self.publisher_ = self.create_publisher(
            JointTrajectory,
            '/arm_controller/joint_trajectory',
            10)
        self.get_logger().info(" Đã khởi tạo Node điều khiển cánh tay (Xoay + Tịnh tiến)!")
    def send_goal(self, target_positions):
        msg = JointTrajectory()
        # Thứ tự khớp: 1 là xoay, 2 là tịnh tiến
        msg.joint_names = ['jointlink1', 'jointlink2']        
        point = JointTrajectoryPoint()
        point.positions = target_positions
        # Vẫn cho chạy từ từ trong 2 giây
        point.time_from_start.sec = 2
        point.time_from_start.nanosec = 0
        msg.points = [point]
        self.publisher_.publish(msg)
        self.get_logger().info(f" Đang di chuyển tới: Khớp xoay={target_positions[0]} rad, Khớp tịnh tiến={target_positions[1]} m")

def main(args=None):
    rclpy.init(args=args)
    node = ArmControllerNode()
    import time
    time.sleep(1) 
    #  CHỈNH VỊ TRÍ TẠI ĐÂY
    # Số 1 (jointlink1): Radian   # Số 2 (jointlink2): Mét (m)
    vi_tri_mong_muon = [0.5, -0.05] 
    node.send_goal(vi_tri_mong_muon)
    rclpy.spin_once(node, timeout_sec=2.0)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()