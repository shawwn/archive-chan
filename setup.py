#!/usr/bin/env python
# coding: utf-8
import codecs
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

with codecs.open('README.rst') as file:
    long_description = file.read()
    if not isinstance(long_description, str):
        long_description = str(long_description, 'utf-8')


setup(
    name='archive-chan',
    version='0.1.1',
    description='Makes a complete hostable archive of imageboard threads including images, HTML, and JSON.',
    long_description=long_description,
    author='Antonizoon Overtwater <antonizoon@bibanon.org>, Daniel Oaks <daniel@danieloaks.net>',
    author_email='antonizoon@bibanon.org',
    maintainer='Shawn Presser <twitter.com/theshawwn>',
    maintainer_email='shawnpresser@gmail.com',
    url='https://github.com/shawwn/archive-chan',
    scripts=['thread-archiver', '4chan-thread-archiver', 'archive-nabber', 'archive-chan'],
    packages=['basc_archiver', 'basc_archiver.sites'],
    package_dir={
        'basc_archiver': 'basc_archiver',
        'basc_archiver.sites': 'basc_archiver/sites',
    },
    install_requires=['requests', 'docopt>=0.5.0', 'BASC-py4chan>=0.5.5'],
    keywords='4chan downloader images json dump',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
