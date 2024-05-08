import os
import shutil
import sys
import subprocess
import zipfile
import requests

import requests
from tqdm import tqdm
import py7zr

proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897",
}

def download_file(url, filename):
    global proxies
    # 发送 GET 请求
    response = requests.get(url, proxies=proxies, stream=True)  # 添加stream=True以启用流下载
    # 确保请求成功
    response.raise_for_status()

    # 获取文件总大小
    total_size = int(response.headers.get('content-length', 0))

    # 打开一个文件并写入内容
    with open(filename, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

download_url = 'https://github.com/niXman/mingw-builds-binaries/releases/download/13.2.0-rt_v11-rev0/x86_64-13.2.0-release-win32-seh-msvcrt-rt_v11-rev0.7z'
save_path = 'mingw.7z'
download_file(download_url, save_path)
extract_to_path = '.'
shutil.rmtree("mingw64", True)
with py7zr.SevenZipFile(save_path, mode='r') as z:
    z.extractall(extract_to_path)
os.remove(save_path)

download_url = 'https://github.com/Kitware/CMake/releases/download/v3.29.3/cmake-3.29.3-windows-x86_64.zip'
save_path = 'cmake.zip'
download_file(download_url, save_path)
extract_to_path = '.'
shutil.rmtree("cmake-3.29.3", True)
with zipfile.ZipFile(save_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)
os.rename("cmake-3.29.3-windows-x86_64", "cmake-3.29.3")
os.remove(save_path)

download_url = 'https://github.com/glfw/glfw/releases/download/3.4/glfw-3.4.zip'
save_path = 'glfw-3.4.zip'
download_file(download_url, save_path)
extract_to_path = '.'
shutil.rmtree('glfw-3.4', True)
# 打开 ZIP 文件并解压全部内容
with zipfile.ZipFile(save_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)
os.remove(save_path)
    
download_url = "https://github.com/ninja-build/ninja/releases/download/v1.12.0/ninja-win.zip"
save_path = 'ninja-win.zip'
download_file(download_url, save_path)
extract_to_path = 'ninja'
shutil.rmtree(extract_to_path, True)
# 打开 ZIP 文件并解压全部内容
with zipfile.ZipFile(save_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)
os.remove(save_path)

LIB_NAME = "glfw-3.4"
BUILD_TYPE = "Release"
LIB_SOURCE = os.path.join(os.path.abspath(os.curdir), LIB_NAME)
LIB_INSTALL = os.path.join(os.path.abspath(os.curdir), "GLFW")
BUILD_DIR = os.path.join(LIB_SOURCE, "build")
shutil.rmtree(BUILD_DIR, True)
shutil.rmtree(LIB_INSTALL, True)
CMAKE_EXECUTABLE = os.path.join(os.path.abspath(os.curdir), "cmake-3.29.3", "bin", "cmake.exe")
MINGW_DIR = os.path.join(os.path.abspath(os.curdir), "mingw64", "bin")
CMAKE_C_COMPILER = os.path.join(MINGW_DIR, "gcc.exe")
CMAKE_CXX_COMPILER = os.path.join(MINGW_DIR, "g++.exe")
CMAKE_MAKE_PROGRAM = os.path.join(os.path.abspath(os.curdir), "ninja", "ninja.exe")
# CMAKE_MAKE_PROGRAM = os.path.join(MINGW_DIR, "mingw32-make.exe")

os.system(f'''set PATH=%PATH%;{MINGW_DIR} && {CMAKE_EXECUTABLE} -S {LIB_SOURCE} -G "Ninja" -B {BUILD_DIR} -DCMAKE_C_COMPILER={CMAKE_C_COMPILER} -DCMAKE_CXX_COMPILER={CMAKE_CXX_COMPILER} -DCMAKE_MAKE_PROGRAM={CMAKE_MAKE_PROGRAM} -DCMAKE_BUILD_TYPE={BUILD_TYPE} --install-prefix {LIB_INSTALL} && {CMAKE_EXECUTABLE} --build {BUILD_DIR} --target install --parallel 8
''')

shutil.copytree(os.path.join(LIB_SOURCE, "deps"), os.path.join(LIB_INSTALL, "include", "deps"))



