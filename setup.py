#!/usr/bin/env python
from setuptools import setup

setup (
    name = 'pfsense_ssh',
    version = '0.0.1',
    description = 'A simple SSH client, including utilities for manipulating pfSense.',
    author = 'Travis Cunningham',
    author_email = 'travcunn@umail.iu.edu',
    packages = ['pfsense_ssh'],
    package_dir = {'pfsense_ssh' : 'pfsense_ssh'},
    install_requires = ['argparse', 'ecdsa', 'paramiko', 'pycrypto',
                        'wsgiref'],
)
