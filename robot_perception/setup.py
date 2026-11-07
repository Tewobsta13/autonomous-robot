from setuptools import find_packages, setup

package_name = 'robot_perception'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tewo',
    maintainer_email='tewobstal@gmail.com',
    description='Visual perception module for a vision-based autonomous mobile robot.',
    license='MIT-0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
             'camera_subscriber = robot_perception.camera_subscriber:main',
        ],
    },
)
