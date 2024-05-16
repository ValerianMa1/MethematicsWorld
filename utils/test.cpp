//
// Created by 23935 on 2024/5/9.
//
#include "dft.h"
#include <iostream>

int main() {
    s_matrix mat(3, 3);  // 创建一个3x3的动态矩阵
    mat <<  1, 2, 3,
            4, 5, 6,
            7, 8, 9;
    std::cout << mat << '\n';
    f_matrix dft_mat = DFT_2D(mat);
    s_matrix idft_mat = IDFT_2D(dft_mat);
    std::cout << dft_mat << '\n';
    std::cout << idft_mat << '\n';
    return 0;
}