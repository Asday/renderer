#!/usr/bin/env python

from glob import glob
import io
from os.path import basename, dirname, join, splitext
import re
from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='hex-roguelike-renderer',
    version='0.0.0',
    license='MIT',
    description='Renderer for hex-based roguelikes.',
    long_description='',
    author='Adam Barnes',
    author_email='sara.and.zuka@gmail.com',
    url='https://github.com/asday/renderer',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    install_requires=[
        'pyglet>=1.3,<1.4',
    ],
)
