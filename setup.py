"""Setup script for boilerplate package."""
import os

from setuptools import find_packages
from setuptools import setup


setup(
    name="boilerplate",  # update this to reflect your project name
    version="1.0.0",
    description="Boilerplate code for basic python package",
    author="Billy Daly",  # change this to your name or org
    author_email="williamdaly422@gmail.com",  # change this to your email
    install_requires=[],
    include_package_data=True,
    package_dir={"": "src"},  # this is required to access code in src/
    packages=find_packages(where="src"),  # same as above
)
