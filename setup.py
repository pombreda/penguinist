"""
Scripts and system tool wrappers for linux

This module is split from penguinist module to platform dependent tool
"""

import sys
import os
import glob

from setuptools import setup, find_packages

VERSION='4.1.0'

setup(
    name = 'penguinist',
    keywords = 'System Management Utility Linux Scripts',
    description = 'Sysadmin utility modules and scripts for linux',
    author = 'Ilkka Tuohela',
    author_email = 'hile@iki.fi',
    version = VERSION,
    url = 'http://tuohela.net/packages/penguinist',
    license = 'PSF',
    zip_safe = False,
    packages = (
        'penguinist',
        'penguinist.log',
    ),
    scripts = glob.glob('bin/*'),
    install_requires = (
        'systematic>=4.0.4',
        'seine>=2.4.1',
    ),
)

