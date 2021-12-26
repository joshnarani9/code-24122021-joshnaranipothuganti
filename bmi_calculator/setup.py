"""
author@joshnarani
"""
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bmi_calculator",
    version="0.1.4",
    author="Joshna Rani",
    author_email="joshnarani97@gmail.com",
    description="bmi_calculator and utils",
    packages=find_packages(include=['bmi_calculator', 'bmi_calculator*']),
    python_requires='>3.7',
    test_suite="tests.test_utils"
)
