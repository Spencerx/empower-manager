# coding: utf-8
from __future__ import print_function, unicode_literals
import sys
import codecs
from setuptools import setup, find_packages
from empower-manager import __version__, __author__, __email__


with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]


def long_description():
    with codecs.open('README.md', 'rb') as f:
        if sys.version_info >= (3, 0, 0):
            return str(f.read())


setup(
    name='empower-manager',
    version=__version__,
    packages=find_packages(),
    author=__author__,
    author_email=__email__,
    description='5G-EmPOWER Command Line Interface',
    long_description=long_description(),
    url='https://github.com/5g-empower/empower-manager',
    download_url='https://github.com/5g-empower/empower-manager/tarball/master',
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'empower-manager = empower-manager.command:main',
        ]
    },
    license='APACHE',
)
