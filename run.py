import os
import shutil

LIB_NAME = "glfw-3.4"
BUILD_TYPE = "Release"
LIB_SOURCE = os.path.join(os.path.abspath(os.curdir), LIB_NAME)
LIB_INSTALL = os.path.join(os.path.abspath(os.curdir), "GLFW")
BUILD_DIR = os.path.join(LIB_SOURCE, "build")
CMAKE_EXECUTABLE = os.path.join(os.path.abspath(os.curdir), "cmake-3.29.3", "bin", "cmake.exe")
MINGW_DIR = os.path.join(os.path.abspath(os.curdir), "mingw64", "bin")
CMAKE_C_COMPILER = os.path.join(MINGW_DIR, "gcc.exe")
CMAKE_CXX_COMPILER = os.path.join(MINGW_DIR, "g++.exe")
CMAKE_MAKE_PROGRAM = os.path.join(os.path.abspath(os.curdir), "ninja", "ninja.exe")

shutil.rmtree("build", True)

os.system(f'''set PATH=%PATH%;{MINGW_DIR} && {CMAKE_EXECUTABLE} -S . -G "Ninja" -B build -DCMAKE_C_COMPILER={CMAKE_C_COMPILER} -DCMAKE_CXX_COMPILER={CMAKE_CXX_COMPILER} -DCMAKE_MAKE_PROGRAM={CMAKE_MAKE_PROGRAM} -DCMAKE_BUILD_TYPE={BUILD_TYPE} && {CMAKE_EXECUTABLE} --build build --parallel 8
''')

os.system(os.path.join(os.path.abspath(os.curdir), "build", "MathematicsWorld.exe"))
