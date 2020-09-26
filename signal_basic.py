#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   signal_basic.py
#@Time    :   2020/09/26 22:04:56
#@Author  :   yinda 
#@Email   :   13616215462@139.com
#@Description:实现信号时域与频域的转换

import numpy as np
import matplotlib.pyplot as plt

'''
假设信号，含有2V的直流分量，50HZ，相位为-30度，幅度为3V的交流信号
含有75HZ，相位90度，幅度1.5V的交流信号
'''
A0 = 2      # 直流分量幅度
A1 = 3      # 频率F1信号的幅度
A2 = 1.5    # 频率F2信号的幅度
F1 = 50     # 信号1频率(HZ)
F2 = 75     # 信号2频率(HZ)
Fs = 256    # 采样频率
P1 = -30    # 信号1相位
P2 = 90     # 信号2相位
N = 256     # 采样点数
t = np.linspace(0, N/Fs, N) # 从0到N/Fs,步长1/Fs

# 原始信号表达式
s = A0 + A1*np.cos(2*np.pi*F1*t+np.pi*P1/180) + A2*np.cos(2*np.pi*F2*t+np.pi*P2/180)

sf = np.fft.fft(s, n=N)     # 傅里叶变换
sf_abs = np.abs(sf)         # 取模

# 换算成实际的模值
sf_abs = sf_abs / (N/2)
sf_abs[0] = sf_abs[0]/2

# 换算成实际的频率
F = np.linspace(0, N, N)*Fs/N

# 计算相位
P = np.linspace(0, N//2, N//2)
for i in range(N//2):
    P[i] = np.angle(sf[i])  # 取相位
    P[i] = P[i]*180/np.pi   # 换算为角度

plt.figure()
plt.subplot(221), plt.plot(t, s), plt.title('raw signal')
plt.subplot(222), plt.plot(t, np.abs(sf)), plt.title('specturm')
plt.subplot(223), plt.plot(F, sf_abs), plt.title('real specturm')
plt.subplot(224), plt.plot(F[0:N//2], P[0:N//2]), plt.title('Angle')
plt.show()

