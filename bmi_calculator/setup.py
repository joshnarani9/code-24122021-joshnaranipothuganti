"""
author@joshnarani
"""
from setuptools import setup, find_packages


def read():
    pass


setup(
    name="bmi_calculator",
    version="0.0.2",
    author="Joshna Rani",
    author_email="joshnarani97@gmail.com",
    description="bmi_calculator and utils",
    packages=find_packages(include=['bmi_calculator', 'bmi_calculator*']),
    python_requires='>3.9',
    test_suite="tests.test_utils"
)
