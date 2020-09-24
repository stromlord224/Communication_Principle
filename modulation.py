import matplotlib.pyplot as plt
import numpy as np

# class modulation:
#     def  __init__(self, m):


if __name__ == "__main__":
    # 创建调制信号
    fs = 51200  # 采样频率：51200HZ
    fm = 200    # 调制信号频率：200HZ
    fc = 1000   # 载波频率：1000HZ
    N = 512     # 采样点数
    t = np.linspace(0, 1/fs, N)   

    # 调制信号modula_signal表达式
    modula_signal = np.cos(2 * np.pi * fm * t)

    # 图像显示
    plt.figure()
    plt.plot(modula_signal)
    plt.show()
