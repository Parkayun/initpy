"""
flask-init
----------
Generate Flask project.
"""

from os import path
from setuptools import setup

long_description = open(
    path.join(
        path.dirname(__file__),
        'README.rst'
    )
).read()

setup(
    name='flask-init',
    version='0.2.3',
    url='https://github.com/Parkayun/flask-init',
    license='MIT',
    author='Ayun Park',
    author_email='iamparkayun@gmail.com',
    description='Generate Flask project',
    long_description=long_description,
    packages=['flask_init'],
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=['six'],
    entry_points={
        'console_scripts': [
            'flask-init=flask_init.run:main',
        ],
    },
)
