from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robonav'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share',package_name,'launch'),glob('launch/*.launch.py')),

        #(os.path.join('share',package_name,'config'),glob('config/*.lua')),
        #(os.path.join('share',package_name,'config'),glob('config/*.yaml')),
        #(os.path.join('share',package_name,'maps'),glob('maps/*.yaml')),
        #(os.path.join('share',package_name,'maps'),glob('maps/*.pgm')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eleclabs',
    maintainer_email='eleclabs@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "robot_core_node = robonav.robot_core:main",
            # "nav2_cmd = robonav.navigation2_command:main",
            # "imu_publisher = robonav.imu_publisher:main",
        ],
    },
)
