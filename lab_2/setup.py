from setuptools import find_packages, setup

package_name = 'lab_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='divyamc',
    maintainer_email='divyamc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_controller = lab_2.turtlesim_controller:main',
            'service = lab_2.service:main',
            'client = lab_2.client:main',
            'turtle_spawner = lab_2.turtle_spawner:main',
            'turtle_killer = lab_2.turtle_killer:main'
        ],
    },
)
