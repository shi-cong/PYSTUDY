#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system('twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'speedups':
    try:
        __import__('pip')
    except ImportError:
        print('Pip required.')
        sys.exit(1)

    os.system('pip install ujson')
    sys.exit()

if sys.argv[-1] == 'test':
    try:
        __import__('py')
    except ImportError:
        print('py.test required.')
        sys.exit(1)

    errors = os.system('py.test test_PYSTUDY.py')
    sys.exit(bool(errors))

packages = [
    'PYSTUDY',
    'PYSTUDY.api',
    'PYSTUDY.image',
    'PYSTUDY.middleware',
    'PYSTUDY.ml',
    'PYSTUDY.net',
    'PYSTUDY.office',
]

install = [
    'bcrypt',
    'scrapy',
    'xlwt',
    'pymongo',
    'pymysql',
    'numpy',
    'pypdf2',
    'reportlab',
    'pytesseract',
    'pillow',
    'pika',
    'requests',
    'tensorflow',
    'tornado',
    'pyyaml',
]


with open('PYSTUDY/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name='PYSTUDY',
    version=version,
    description='learning python',
    author='shi-cong',
    author_email='shi_cong@icloud.com',
    url='https://github.com/shi-cong/PYSTUDY',
    packages=packages,
    license='Apache License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    tests_require=['pytest'],
    install_requires=install,
)
