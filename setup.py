# -*- coding: utf-8 -*-
__author__ = 'chq'

"""
@author:joko
@time: 2018/03/10 
"""
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='Auto_Analysis',
    keywords='',
    version=1.0,
    packages=find_packages(),
    url='',
    license='MIT',
    author='chq',
    author_email='laoqi1988_f1@126.com',
    description='',
    install_requires=[
        'pyyaml', 'matplotlib', 'selenium', 'termcolor'
    ]
)
