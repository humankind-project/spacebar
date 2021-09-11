#!/usr/bin/env python

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
	name="pip_template",
	version="0.1.0",
	description="Template for building pip packages",
	long_description=long_description,
	author="Brandon Sexton",
	author_email="brandon.sexton.1@outlook.com",
	entry_points={'console_scripts': ['cmd_name'='scriptname:runmethod']}
	packages=find_packages()
	)
