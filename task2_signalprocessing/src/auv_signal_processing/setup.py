from setuptools import find_packages, setup

package_name = 'auv_signal_processing'

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
    maintainer='krishna',
    maintainer_email='ph25b1002@iiitdm.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
	    'console_scripts': [
            'publisher = auv_signal_processing.publisher_node:main',
            'processor = auv_signal_processing.processor_node:main',
            'output = auv_signal_processing.output_node:main',
        ],
    },
)
