#!/usr/bin/python

from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

import numpy as np

ext_modules = [
    Extension('_pgenlib',
              sources = ['pgenlib/_pgenlib.pyx', 'pgenlib/pgenlib_python_support.cpp', 'pgenlib/pgenlib_internal.cpp', 'pgenlib/plink2_base.cpp'],
              language = "c++",
              # do not compile as c++11, since cython doesn't yet support
              # overload of uint32_t operator
              # extra_compile_args = ["-std=c++11", "-Wno-unused-function"],
              # extra_link_args = ["-std=c++11"],
              extra_compile_args = ["-std=c++98", "-Wno-unused-function"],
              extra_link_args = ["-std=c++98"],
              include_dirs = [np.get_include()]
              )
    ]

setup(name = 'pgenlib',
      version = '0.7',
      description = "Wrapper for pgenlib's basic reader and writer.",
      ext_modules = cythonize(ext_modules))
