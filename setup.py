#!/usr/bin/env python
import os
import sys
from pathlib import Path

from cmake_build_extension import BuildExtension, CMakeExtension
from setuptools import setup
from distutils import sysconfig

cmake_options = []
# for arm 64 on MacOS
if "macosx_arm64" in os.environ.get("CIBW_BUILD", ""):
    # cross build
    cmake_options.append("-DCMAKE_OSX_ARCHITECTURES=arm64")

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
                            "-DPYTHON_INCLUDE_DIR="+sysconfig.get_config_var('INCLUDEPY'),
                            "-DBUILD_BY_PIP=ON",
                            *cmake_options,
                       ]),
    ],
    cmdclass=dict(build_ext=BuildExtension),
)
