#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup  # pylint: disable=import-error
from setuptools import find_packages

setup(name="fluffy_octo_couscous",
		version="0.0.1",
		description="A simple program for Gemini API",
		packages=find_packages(),
		install_requires=[
            "google-generativeai>=0.8.3",
            "googletrans==4.0.0-rc1",
            "PyYaml >= 6.0",
            "pytest >= 8.3.3",
            "SQLAlchemy >= 2.0.36",
            "alembic >= 1.14.0",
            "beautifulsoup4 >= 4.12.3"
		],
		entry_points={
		},
		classifiers=[
				"Development Status :: 3 - Alpha",
				"Intended Audience :: Developers",
				"Operating System :: POSIX",
				"Programming Language :: Python :: 3.12.3",
		],
		)

# vim: tabstop=4 shiftwidth=4
