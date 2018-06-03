# /usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name="Photo Organiser",
    description="A utility for organising photos based on date",
    author="Jose Sebastian",
    author_email="joesaby@gmail.com",
    url="https://github.com/joesaby/photo-organiser",
    version="0.0.1",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
