#!/usr/bin/env python
import sys
from pathlib import Path

from cmake_build_extension import BuildExtension, CMakeExtension
from setuptools import setup
from distutils import sysconfig

setup(
    ext_modules=[
        CMakeExtension(name="OpenBabel",
                       install_prefix="openbabel",
                       source_dir=str(Path(__file__).parent.absolute() / "source"),
                       cmake_configure_options=[
                            "-DPYTHON_EXECUTABLE=" + sys.executable,
                            "-DCMAKE_BUILD_TYPE=Release",
                            "-DWITH_INCHI=ON",
                            "-DPYTHON_BINDINGS=ON",
                            "-DRUN_SWIG=ON",
                            "-DPYTHON_INCLUDE_PATH="+sysconfig.get_config_var('INCLUDEPY'),
                            "-DBUILD_BY_PIP=ON",
                       ]),
    ],
    cmdclass=dict(build_ext=BuildExtension),
)