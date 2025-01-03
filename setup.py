from setuptools import setup

package_name = 'usage_tracker'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rin Takahashi',
    maintainer_email='s23c1083vp@s.chibakoudai.jp',
    description='A ROS 2 package for tracking PC usage time',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'usage_tracker_node = usage_tracker.usage_tracker_node:main',
        ],
    },
)

