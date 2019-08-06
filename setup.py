#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import pip
from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


LONG_DESCRIPTION = """tiny cache file manager for data analysis"""

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ str(requirement.req) for requirement in parse_requirements('requirements.txt', session="production") ]

setup_requirements = [
    # TODO(takahi-i): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='hideout',
    version='0.2.5',
    description="",
    long_description=LONG_DESCRIPTION,
    author="Takahiko Ito",
    author_email='takahiko03@gmail.com',
    url='https://github.com/takahi-i/hideout',
    packages=find_packages(),
    entry_points={
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
