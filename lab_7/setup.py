from setuptools import find_packages, setup
import glob
import os

package_name = 'lab_7'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob.glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob.glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='divyamc',
    maintainer_email='divyamchandalia3@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "extract_road = lab_7.extract_road:main",
            "capture = lab_7.capture_image:main",
            "line_follower = lab_7.line_follower:main",
        ],
    },
)
