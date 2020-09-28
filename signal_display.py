import matplotlib.pyplot as plt
import numpy as np

class display_signal:
    def __init__(self, fs, N, x=1, y=1, title=''):
        plt.figure(), plt.suptitle(title)

        self.fs = fs
        self.N = N
        self.t_t = np.linspace(0, N/fs, N)                 # 时域坐标
        self.t_s = np.linspace(-N//2, N//2, N) * fs/N      # 频域坐标

        self.count = 1
        self.x = x      
        self.y = y
    
    def display_time(self, signal, title=''):
        plt.subplot(self.x, self.y, self.count)
        self.count = self.count + 1

        plt.plot(self.t_t, signal), plt.title(title)

    
    def display_sprcturm(self, signal, title=''):
        signal_fft = np.fft.fftshift(np.fft.fft(signal))    # 傅里叶变换
        signal_fft_abs = np.abs(signal_fft)     # 取模

        # 换算成实际的模值
        signal_fft_abs = signal_fft_abs / (self.N/2)
        # signal_fft_abs[0] = signal_fft_abs[0] / 2

        plt.subplot(self.x, self.y, self.count)
        self.count = self.count + 1

        plt.plot(self.t_s, signal_fft_abs), plt.title(title)

    