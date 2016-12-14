"""Setup.py for data-structures repo."""

from setuptools import setup

setup(
    name="data-structures",
    description="Implementation of a Linked List.",
    version=0.1,
    author="Colin Lamont, Conor Clary",
    author_email="sclary50@gmail.com, colinLamont@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=['data-structures'],
    install_requires=['ipython'],
    extras_require={
        "test": ['tox', 'pytest', 'pytest-watch', 'pytest-cov']
    },
)
