"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the lrn_databricks_dab project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import lrn_databricks_dab

setup(
    name="lrn_databricks_dab",
    version=lrn_databricks_dab.__version__,
    url="https://databricks.com",
    author="griff182uk@yahoo.co.uk",
    description="wheel file based on lrn_databricks_dab/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        "packages": [
            "main=lrn_databricks_dab.main:main"
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
