from setuptools import setup
import os
from glob import glob

package_name = 'urdf1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Chỗ này giúp ROS tìm thấy file Launch, URDF và YAML của bạn
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lequang',
    maintainer_email='lequang@todo.todo',
    description='Dự án Robot điều khiển 4 bánh và tay máy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Lệnh để bạn chạy script điều khiển sau này
            'super_teleop = urdf1.super_teleop:main'
        ],
    },
)