# 指定CMake的最低版本要求
cmake_minimum_required(VERSION 3.20)

# set(CMAKE_C_COMPILER, ${CMAKE_SOURCE_DIR}/mingw64/bin/gcc.exe)
# set(CMAKE_CXX_COMPILER, ${CMAKE_SOURCE_DIR}/mingw64/bin/g++.exe)
# set(CMAKE_MAKE_PROGRAM, ${CMAKE_SOURCE_DIR}/mingw64/ninja.exe)

# 设置项目名称
project(MathematicsWorld)

# 设置使用的C++标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(GLFW_DIR ${CMAKE_SOURCE_DIR}/GLFW)
set(GLAD_DIR ${CMAKE_SOURCE_DIR}/GLFW/include/deps/glad)

include_directories(${CMAKE_SOURCE_DIR}/GLFW/include/deps)
include_directories(${CMAKE_SOURCE_DIR}/Eigen/include/eigen3/Eigen)
include_directories(${GLAD_DIR})
include_directories(${GLFW_DIR}/include/GLFW)
link_directories(${GLFW_DIR}/lib/)

# 添加一个可执行文件
add_executable(MathematicsWorld main.cpp
        utils/dft.cpp
        utils/dft.h)
target_link_libraries(MathematicsWorld glfw3)
add_executable(DFT_test utils/test.cpp
        utils/dft.cpp
        utils/dft.h)
#target_link_libraries(DFT_test stdc++)
