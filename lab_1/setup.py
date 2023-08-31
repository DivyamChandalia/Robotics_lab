from setuptools import find_packages, setup

package_name = 'lab_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'launch', 'launch_ros'],
    zip_safe=True,
    maintainer='divyamc',
    maintainer_email='divyamc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node = lab_1.test1:main',
            'publisher = lab_1.publisher:main',
            'subscriber = lab_1.subscriber:main',
            'num_pub = lab_1.number_publisher:main',
            'num_count = lab_1.number_counter:main'

        ],
    },
)
