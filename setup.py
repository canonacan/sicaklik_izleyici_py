from setuptools import find_packages, setup

package_name = 'sicaklik_izleyici_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='muhammed',
    maintainer_email='canonacan26@gmail.com',
    description='ROS 2 sicaklik sensoru ve izleyici',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor = sicaklik_izleyici_py.sensor:main',
            'izleyici = sicaklik_izleyici_py.izleyici:main',
        ],
    },
)
