cmake_minimum_required(VERSION 3.11)
project(ObabelPythonDistributions CXX)

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
    DESTINATION ${SKBUILD_PLATLIB_DIR}
  )
endif()