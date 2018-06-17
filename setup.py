
from setuptools import setup, find_packages

install_requires = [
    'bottle'
]

setup(
    name='appname',
    version='0.1.0',
    packages=find_packages(),
    package_data={ '': ['*.html'] },
    entry_points={
        'console_scripts': [ 'appname=appname.__main__:main' ]
    },
    install_requires=install_requires
)
