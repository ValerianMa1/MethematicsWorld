//
// Created by 23935 on 2024/5/9.
//

#ifndef MATHEMATICSWORLD_DFT_H
#define MATHEMATICSWORLD_DFT_H
#include "Dense"

using f_matrix = Eigen::Matrix<std::complex<double>, Eigen::Dynamic, Eigen::Dynamic>;
using s_matrix = Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic>;

f_matrix DFT_2D(s_matrix& f);
s_matrix IDFT_2D(f_matrix& F);
#endif //MATHEMATICSWORLD_DFT_H
