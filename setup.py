#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


requirements = []
with open("requirements.txt") as fin:
    for r in fin:
        requirements.append(r.rstrip('\n'))

setup_requirements = [
    'pytest-runner',
    # TODO(harshrpg): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: Put package test requirements here
]

setup(
    name='FC2',
    version='0.1.0',
    description="This software will calculate the most efficient routes for an aircraft as per the fuel consumption",
    long_description=readme + '\n\n' + history,
    author="Harsh Gupta",
    author_email='harsh.gupta@ucdconnect.ie',
    url='https://github.com/harshrpg/FC2',
    packages=find_packages(include=['FC2']),
    entry_points={
        'console_scripts': [
            'FC2=FC2.cli:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='FC2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
