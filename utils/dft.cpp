//
// Created by 23935 on 2024/5/9.
//

#include "dft.h"
#include "Dense"

#include <string>
#include <complex>
#include <cmath>
#include <iostream>

using namespace Eigen;

#ifndef M_PI
constexpr const static double M_PI = 3.14159265358979323846;
#endif
constexpr const static double two_pi = 2.0 * M_PI;

f_matrix DFT_2D(s_matrix& f){
    constexpr const static std::complex<double> i(0, 1);
    Index M = f.rows();
    Index N = f.cols();
    f_matrix F(M, N);
    for (int u = 0; u < M; ++u) {
        for (int v = 0; v < N; ++v) {
            std::complex<double> sum(0, 0);
            for (int x = 0; x < M; ++x) {
                for (int y = 0; y < N; ++y) {
                    sum += f(x, y) * exp(-i*two_pi*(((double)u*x/(double)M) + ((double)v*y/(double)N)));
                }
            }
            F(u, v) = sum;
        }
    }
    return F;
}

s_matrix IDFT_2D(f_matrix& F){
    constexpr const static std::complex<double> i(0, 1);
    Index M = F.rows();
    Index N = F.cols();
    const double Inv_MN = 1.0 / (double)(M*N);
    s_matrix f(M, N);
    for (int x = 0; x < M; ++x) {
        for (int y = 0; y < N; ++y) {
            std::complex<double> sum(0, 0);
            for (int u = 0; u < M; ++u) {
                for (int v = 0; v < N; ++v) {
                    sum += F(u, v) * exp(i*two_pi*(((double)u*x/(double)M) + ((double)v*y/(double)N)));
                }
            }
            f(x, y) = (Inv_MN * sum).real();
        }
    }
    return f;
}