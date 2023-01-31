# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-17 17:34:50
# @Last Modified by:   p-chambers
# @Last Modified time: 2017-06-29 12:22:12
from setuptools import setup, find_packages

version = '1.4.0'

setup(
    name='astra',
    version=version,
    description='ASTRA high altitude balloon flight planner',
    packages=find_packages(),
    include_package_data=True,
    scripts=['bin/astra-sim'],
    # package_data={'': ['*.dat']},
    install_requires=["numpy", "scipy", "grequests", "six", "deap"],
    author='Niccolo Zapponi, Paul Chambers',
    author_email='nz1g10@soton.ac.uk, P.R.Chambers@soton.ac.uk',
)
