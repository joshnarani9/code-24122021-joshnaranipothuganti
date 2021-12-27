"""
author@joshnarani
"""
import os
from setuptools import setup, find_packages

requires = (
    "numpy==1.21.5",
    "pandas==1.3.5",
    "json5==0.9.5"
)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bmi_calculator",
    version="0.1.8",
    author="Joshna Rani",
    author_email="joshnarani97@gmail.com",
    description="bmi_calculator and utils",
    packages=find_packages(include=['bmi_calculator', 'bmi_calculator*']),
    python_requires='>3.7',
    install_requires=requires,
    test_suite="tests.test_utils"
)
