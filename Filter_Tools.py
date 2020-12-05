import numpy as np


class Filters:
    def __init__(self):
        self.cutoff_freq = 0
        self.signal = np.ones(512)

    def High_Pass_Filter(self, cutoff_freq, signal):
        '''
        理想高通滤波器
        :param cutoff_freq: 截止频率
        :param signal: 信号
        :return: 滤波器
        '''
        self.cutoff_freq = cutoff_freq
        self.signal = signal

        H = np.ones(len(signal))
        for i in range(len(signal)):
            if cutoff_freq >= signal[i] >= -cutoff_freq:
                H[i] = 0
        return H

    def Low_Pass_Filter(self, cutoff_freq, signal):
        '''
        理想低通滤波器
        :param cutoff_freq: 截止频率
        :param signal:      信号
        :return:            滤波器
        '''
        self.cutoff_freq = cutoff_freq
        self.signal = signal

        H = np.zeros(len(signal))
        for i in range(len(signal)):
            if cutoff_freq >= signal[i] >= -cutoff_freq:
                H[i] = 1
        return H