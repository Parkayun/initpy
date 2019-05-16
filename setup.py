"""
initpy
------
Generate Python project.
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
    name='initpy',
    version='0.2.4',
    url='https://github.com/Parkayun/initpy',
    license='MIT',
    author='Ayun Park',
    author_email='iamparkayun@gmail.com',
    description='Generate Python project',
    long_description=long_description,
    packages=['initpy', 'initpy.templates'],
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
    entry_points={
        'console_scripts': [
            'init.py=initpy.run:main',
        ],
    },
)
