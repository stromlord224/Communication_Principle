import numpy as np
from Filter_Tools import Filters
from signal_display import display_signal


class Demodulation:
    def __init__(self, fs, N, s_modula):
        self.N = N      # 采样频率
        self.fs = fs    # 采样点数
        self.s_modula = s_modula    # 调制信号
        self.t = np.linspace(0, N / fs, N)                  # 时域坐标
        self.t_s = np.linspace(-N // 2, N // 2, N) * fs / N # 频域坐标

    def Coherent_Demodulation(self, signal_carried, cutoff_freq, display_flag=False):
        '''
        :param signal_carried:  载波信号
        :param H_cutoff_freq:   高通滤波截止频率
        :param display_flag:    显示标志位
        :return:
        '''

        signal_modulation = self.s_modula
        t_s = self.t_s
        signal_operate = signal_carried * signal_modulation
        operate_fft = np.fft.fftshift(np.fft.fft(signal_operate))

        # 对于AM信号，高通滤波去除直流分量
        # H = Filters().High_Pass_Filter(3, t_s)
        # operate_fft = operate_fft * H
        # signal_operate = np.fft.ifft(np.fft.ifftshift(operate_fft))

        # 低通滤波
        H = Filters().Low_Pass_Filter(cutoff_freq, t_s)
        Low_fft = operate_fft * H
        signal_re = np.fft.ifft(np.fft.ifftshift(Low_fft))

        if display_flag:
            demoula_show = display_signal(self.fs, self.N, 2, 2)
            demoula_show.display_time(signal_operate, 'Mul_Signal')
            demoula_show.display_sprcturm(signal_operate, 'sprcturm of Mul_Signal')
            demoula_show.display_time(signal_re, 'Operate_Signal')
            demoula_show.display_sprcturm(signal_re, 'sprcturm of Operate_Signal')