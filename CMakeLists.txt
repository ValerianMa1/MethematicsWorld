# 指定CMake的最低版本要求
cmake_minimum_required(VERSION 3.10)

# 设置项目名称
project(MathematicsWorld)

# 设置使用的C++标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 添加一个可执行文件
add_executable(MathematicsWorld main.cpp)
