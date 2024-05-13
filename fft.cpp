#define _USE_MATH_DEFINES
#include<iostream>
#include<algorithm>
#include<complex>
#include <cmath>
#include<vector>
#include<random>
using namespace std;

struct WaveVector
{
    //kx和ky是一个波数的两个分量
    double kx,ky;
    //对应波数的频谱值，为复数，有复数模长（绝对值）和相位（角度）表示波的相位偏移
    complex<double> spectrumValue;
};





/// @brief 
/// @param A 菲利普频谱中的常数因子，表示波浪的总能量。它决定了生成的海洋波动的整体规模大小
/// @param windSpeed 风速，用于在菲利普频谱中模拟风的影响
/// @param L 特征波长，用来决定波浪的主要规模。在菲利普频谱中，L = windSpeed^2 / g, 其中 g 是重力加速度
/// @param N 生成频谱的网格大小，即在波数域中我们划分的格子数。网格的大小直接影响了生成波浪场的分辨率
/// @param gridSize 一个格子在实际空间中的大小，它决定了模拟的海洋表面的实际尺寸
/// @return 
vector<WaveVector> generatePhillipsSpectrum(double A,double windSpeed,double L,int N,double gridSize) {
    //创建模型参数B
    double B = L * L * windSpeed * windSpeed / 9.81;
    //准备随机生成器和分布
    std::default_random_engine generator;
    std::uniform_real_distribution<double> distribution(0.0, 2.0 * M_PI);
    vector<WaveVector> spectrum; // Declare the spectrum vector
    for(int m = 0;m < N; ++m){
        for(int n = 0;n < N; ++n){
            //计算波数向量
            double kx = (2 * M_PI / (N * gridSize)) * (m - N / 2);
            double ky = (2 * M_PI / (N * gridSize)) * (n - N / 2);
            double k = sqrt(kx * kx + ky * ky);
            complex<double> spectrumValue;

            if(k == 0){
                spectrumValue = 0;
            }else{
                //根据菲利普频谱模型计算频谱密度
                double Pk = A * exp(-1 / (k * k * B)) / (k * k * k * k) * exp(-k * k * L * L);
                //随机生成相位
                double phi = distribution(generator);
                //构造复数频谱值
                spectrumValue = Pk * std::complex<double>(cos(phi),sin(phi));
            }
            //存储波数向量和其对应的频谱值
            spectrum.push_back({kx,ky,spectrumValue});
        }
    }
    return spectrum;
}

