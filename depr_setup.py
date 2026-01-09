#!/usr/bin/env python3
"""Setup script for spectrAI package."""

from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="spectrai",
    version="1.0.0",
    author="Qichen",
    author_email="",  # Add your email if desired
    description="A PyQt5-based spectral image annotation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UGarCil/spectrAI",  # Update if needed
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyQt5>=5.15.0",
        "Pillow>=8.0.0",
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "spectrai=src.spectrai:main",
            "spectrai-annotator=src.imageAnnotator:main",
        ],
    },
    include_package_data=True,
    package_data={
        "src": [
            "ui/*.ui",
            "ui/icons/*.png",
            "ui/icons/*.ai",
        ],
    },
    zip_safe=False,
)