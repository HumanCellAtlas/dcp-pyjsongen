#!/usr/bin/env python

import os, glob
from setuptools import setup, find_packages

install_requires = [line.rstrip() for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))]

setup(
    name="pyjsongen",
    version="0.0.1",
    url='https://github.com/HumanCellAtlas/dcp-pyjsongen',
    license='Apache Software License',
    author='Human Cell Atlas contributors',
    author_email='tsmith12@ucsc.edu',
    description='A tool for generating JSON data from a JSON schema.',
    install_requires=install_requires,
    extras_require={
        ':python_version < "3.5"': ['typing >= 3.6.2, < 4'],
    },
    packages=find_packages(exclude=['test']),
    platforms=['MacOS X', 'Posix'],
    zip_safe=False,
    include_package_data=True,
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
