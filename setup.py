# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]



version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bootstrap/bootstrap.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-bootstrap",
    packages = ["bootstrap"],
    install_requires=requirements,
    entry_points = {
        "console_scripts": ['bootstrap = bootstrap.bootstrap:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Firstname Lastname",
    author_email = "firstname.lastname@google.com",
    url = "http://gehrcke.de/2014/02/distributing-a-python-command-line-application",
    test_suite='tests',
    tests_require=test_requirements
)
