# RoboComp global CMake
cmake_minimum_required(VERSION 3.0)
project(robocomp_libs
        VERSION 2022.10.15
        DESCRIPTION "Robocomp framework libs"
        LANGUAGES CXX )

#variable_watch(Ice_LIBRARIES)
#variable_watch(CMAKE_SOURCE_DIR)


string(TOLOWER ${PROJECT_NAME} PROJECT_NAME_LOWER)

#Set RoboComp directories
set(RoboComp_LIBS_DIR ${CMAKE_SOURCE_DIR}/libs)
# Find universal dependencies
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/modules/" ${CMAKE_MODULE_PATH})

# Release/Debug specific flags
if(CMAKE_BUILD_TYPE STREQUAL "Release" OR CMAKE_BUILD_TYPE STREQUAL "RelWithDebInfo")
  add_definitions("-DBOOST_DISABLE_ASSERTS -DEIGEN_NO_DEBUG")
endif()

# Update the documentation string of CMAKE_BUILD_TYPE for GUIs
SET(CMAKE_BUILD_TYPE "${CMAKE_BUILD_TYPE}" CACHE STRING
    "Choose the type of build, options are: None Debug Release RelWithDebInfo MinSizeRel Maintainer."
    FORCE)

set(RoboComp_VERSION 2022.10.15 CACHE STRING "RoboComp version")

include(${CMAKE_SOURCE_DIR}/cmake/modules/qt.cmake)


# Add an "uninstall" target
configure_file("${CMAKE_SOURCE_DIR}/cmake/uninstall_target.cmake.in"
               "${CMAKE_SOURCE_DIR}/uninstall_target.cmake" IMMEDIATE @ONLY)
add_custom_target(uninstall "${CMAKE_COMMAND}" -P
                  "${CMAKE_SOURCE_DIR}/uninstall_target.cmake")


add_subdirectory(libs)



add_custom_target(mrproper
  COMMAND ${CMAKE_MAKE_PROGRAM} clean
   COMMAND find $ENV{ROBOCOMP} -name CMakeFiles -exec rm -rf {} "\\;"
   COMMAND find $ENV{ROBOCOMP} -name CMakeCache.txt -exec rm {} "\\;"
   COMMAND find $ENV{ROBOCOMP} -name cmake_install.cmake -exec rm {} "\\;"
   COMMAND find $ENV{ROBOCOMP} -name Makefile -exec rm {} "\\;"
   COMMAND find $ENV{ROBOCOMP} -name *.kd* -exec rm {} "\\;"
   COMMAND find $ENV{ROBOCOMP} -name *_moc* -exec rm {} "\\;"
   COMMAND find $ENV{ROBOCOMP} -name Makefile -exec rm {} "\\;"
)
