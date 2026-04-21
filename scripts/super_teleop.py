import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration
import sys, select, termios, tty

msg = """
========================================
    SUPER TELEOP - ROBOT CONTROL
========================================
Di chuyển Xe (WASD):      Tay máy (UJKL):
    w : Tiến                u : Khớp 1 Lên (+)
    s : Lùi                 j : Khớp 1 Xuống (-)
    a : Xoay Trái           i : Khớp 2 Ra (+)
    d : Xoay Phải           k : Khớp 2 Vào (-)
    space : DỪNG XE         o : Reset tay máy

q : Thoát chương trình
----------------------------------------
"""

class SuperTeleop(Node):
    def __init__(self):
        super().__init__('super_teleop_node')
        # Đã sửa lại đúng tên topic nhận lệnh của xe
        self.wheel_pub = self.create_publisher(Twist, '/mobile_base_controller/cmd_vel_unstamped', 10)
        self.arm_pub = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.j1_pos = 0.0
        self.j2_pos = 0.0

    def move_wheels(self, x, z):
        tw = Twist()
        tw.linear.x = float(x)
        tw.linear.y = 0.0
        tw.linear.z = 0.0
        tw.angular.x = 0.0
        tw.angular.y = 0.0
        tw.angular.z = float(z)
        self.wheel_pub.publish(tw)

    def update_arm(self, dj1, dj2):
        self.j1_pos += dj1
        self.j2_pos += dj2
        traj = JointTrajectory()
        traj.joint_names = ['jointlink1', 'jointlink2']
        p = JointTrajectoryPoint()
        p.positions = [float(self.j1_pos), float(self.j2_pos)]
        p.time_from_start = Duration(sec=0, nanosec=200000000)
        traj.points.append(p)
        self.arm_pub.publish(traj)

def get_key(settings):
    tty.setraw(sys.stdin.fileno())
    r, _, _ = select.select([sys.stdin], [], [], 0.1)
    key = sys.stdin.read(1) if r else ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main():
    settings = termios.tcgetattr(sys.stdin)
    rclpy.init()
    node = SuperTeleop()
    l_vel, a_vel = 0.4, 0.8
    try:
        print(msg)
        while True:
            k = get_key(settings)
            
            # --- Đã tráo đổi lệnh để phù hợp với hệ tọa độ xe của bạn ---
            if k == 'w': node.move_wheels(0.0, a_vel)     # Tiến
            elif k == 's': node.move_wheels(0.0, -a_vel)  # Lùi
            elif k == 'a': node.move_wheels(l_vel, 0.0)   # Xoay trái
            elif k == 'd': node.move_wheels(-l_vel, 0.0)  # Xoay phải
            elif k == ' ': node.move_wheels(0.0, 0.0)     # Phanh
            
            # --- Tay máy giữ nguyên ---
            elif k == 'u': node.update_arm(0.1, 0.0)
            elif k == 'j': node.update_arm(-0.1, 0.0)
            elif k == 'i': node.update_arm(0.0, 0.02)
            elif k == 'k': node.update_arm(0.0, -0.02)
            elif k == 'o': 
                node.j1_pos, node.j2_pos = 0.0, 0.0
                node.update_arm(0.0, 0.0)
            elif k == 'q': break
    finally:
        node.move_wheels(0.0, 0.0)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()