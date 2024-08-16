cmake_minimum_required(VERSION 3.11)
project(ObabelPythonDistributions CXX)

find_package(Python REQUIRED COMPONENTS Interpreter)
execute_process(COMMAND ${Python_EXECUTABLE} -m cmeel cmake OUTPUT_VARIABLE CMEEL_PREFIX_PATH OUTPUT_STRIP_TRAILING_WHITESPACE)
set(EIGEN3_INCLUDE_DIR ${CMEEL_PREFIX_PATH}/include/eigen3)
message(STATUS EIGEN3_INCLUDE_DIR=${EIGEN3_INCLUDE_DIR})

set(CMAKE_INSTALL_PREFIX ${SKBUILD_PLATLIB_DIR})

# download OpenBabel to ${OBABEL_SOURCE_ROOT}
include(FetchContent)
FetchContent_Declare(openbabel
  GIT_REPOSITORY    https://github.com/njzjz/openbabel
  GIT_TAG           ${OBABEL_VERSION}
)
FetchContent_GetProperties(openbabel)
if(NOT openbabel_POPULATED)
  FetchContent_Populate(openbabel)
  add_subdirectory(${openbabel_SOURCE_DIR} ${openbabel_BINARY_DIR})
  install(
    DIRECTORY ${CMAKE_SOURCE_DIR}/openbabel/
    DESTINATION ${SKBUILD_PLATLIB_DIR}/openbabel
  )
endif()
