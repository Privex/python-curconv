#!/usr/bin/env python3
"""
+===================================================+
|                 © 2021 Privex Inc.                |
|               https://www.privex.io               |
+===================================================+
|                                                   |
|        Python Currency Converter CLI              |
|        License: X11/MIT                           |
|                                                   |
|        Core Developer(s):                         |
|                                                   |
|          (+)  Chris (@someguy123) [Privex]        |
|                                                   |
+===================================================+

Python Currency Converter CLI - A small CLI tool for quick currency conversions on the command line
Copyright (c) 2021    Privex Inc. ( https://www.privex.io )

Official Repo: https://github.com/Privex/python-curconv

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name(s) of the above copyright holders shall not be used in advertising or
otherwise to promote the sale, use or other dealings in this Software without prior written authorization.
"""

from setuptools import setup, find_packages
from privex.curconv.version import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='privex_curconv',

    version=VERSION,

    description='Python Currency Converter CLI - A small CLI tool for quick currency conversions on the command line',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Privex/python-curconv",
    author='Chris (Someguy123) @ Privex',
    author_email='chris@privex.io',

    license='MIT',
    install_requires=[
        'privex-helpers>=3', 'privex-loghelper', 'httpx[http2]', 'python-dotenv',
        'async-property', 'aiosqlite>=0.12', 'privex-db>=0.9.2'
    ],
    extras_require=dict(
        cache=['privex-helpers[cache]'],
        redis=['aioredis>=1.3', 'hiredis', 'redis'],
        memcached=['pylibmc', 'aiomcache'],
    ),
    packages=find_packages(),
    scripts=['bin/conv'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
