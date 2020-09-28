import matplotlib.pyplot as plt
import numpy as np
from signal_display import display_signal

class modulation:
    def  __init__(self, fs, N):
        '''
        创建变量t
        @param fs: 采样频率
        @param N:  采样点数
        '''
        self.N = N
        self.fs = fs
        self.t = np.linspace(0, N/fs, N)               # 时域坐标
        self.t_s = np.linspace(-N//2, N//2, N) * fs/N   # 频域坐标
        self.s_m = self.t
        self.s_c = self.t
    
    def modula_signal(self, fm, Am):
        '''
        创建基带调制信号
        @param fm: 调制信号频率
        @param Am: 调制信号幅度
        @return: 基带调制信号
        '''
        self.s_m = Am * np.cos(2 * np.pi * fm * self.t)
        return self.s_m

    def carried_signal(self, fc, Ac):
        '''
        创建载波信号
        @param fc: 载波频率
        @param Ac: 载波幅度
        @return: 载波信号
        '''
        self.s_c = Ac * np.cos(2 * np.pi * fc * self.t)
        return self.s_c
    
    def Amplitude_Modulation(self, A0):
        '''
        常规双边带调制，简称调幅(AM)
        @param A0: 直流偏置
        @return: 调幅信号
        '''
        s_Am = (A0 + self.s_m) * self.s_c
        return s_Am

    def DSB_Modulation(self):
        """
        抑制载波双边带信号：Double Side Band with Suppressed Carrier
        @return: 双边带信号
        """
        s_DSB = self.s_m * self.s_c
        return s_DSB

    def SSB_Modulation_filter(self, fc):
        '''
        单边带调制——滤波法
        @param fc: 载波频率
        '''
        s_DSB = self.DSB_Modulation()        # 产生一个双边带信号
        s_fft = np.fft.fftshift(np.fft.fft(s_DSB))  # 傅里叶变换

        # 设计低通滤波器
        t_s = self.t_s
        H = np.ones((len(t_s)))
        for i in range(len(t_s)):
            if t_s[i] <= fc and t_s[i] >= -fc:
                H[i] = 0

        SSB_fft = s_fft * H

        plt.figure()
        plt.subplot(311), plt.plot(t_s, np.abs(s_fft))
        plt.subplot(312), plt.plot(t_s, H)
        plt.subplot(313), plt.plot(t_s, np.abs(SSB_fft))
        return SSB_fft



if __name__ == "__main__":
    N = 512    # 采样点数
    fs = 512   # 采样频率
    modula = modulation(fs, N)

    fm = 8      # 调制信号频率
    Am = 2      # 调制信号幅度
    signal_modula = modula.modula_signal(fm, Am)
    
    fc = 64     # 载波频率
    Ac = 2      # 载波信号幅度
    signal_carried = modula.carried_signal(fc, Ac)
    
    A0 = 2     # 直流偏量，若直流偏量小于调制信号幅度，则会出现“过调幅”现象，无法包络检波
    modula_AM = modula.Amplitude_Modulation(A0)     # 常规双边带调制，AM

    modula_DSB = modula.DSB_Modulation()   # 抑制载波双边带信号，DSB，全部功率用于信息传输

    modula.SSB_Modulation_filter(fc)

    t_t = np.linspace(0, N/fs, N)       # 时域坐标
    t_s = np.linspace(0, N, N) * fs/N   # 频域坐标
    # 显示调制信号和载波
    signal_show = display_signal(fs, N, 2, 2, title='Raw Signal')
    signal_show.display_time(signal_modula, title='modulated signal')
    signal_show.display_sprcturm(signal_modula, title='specturm of modulated signal')
    signal_show.display_time(signal_carried, title='carried signal')
    signal_show.display_sprcturm(signal_carried, title='specturm of carrried signal')
    
    # 显示AM信号
    AM_show = display_signal(fs, N, 2, 1)
    AM_show.display_time(modula_AM, 'AM signal')
    AM_show.display_sprcturm(modula_AM, 'spectrum of AM signal')

    # 显示DSB信号
    DSB_show = display_signal(fs, N, 2, 1)
    DSB_show.display_time(modula_DSB, 'DSB signal')
    DSB_show.display_sprcturm(modula_DSB, 'spectrum of DSB signal')

    # 显示SSB信号
    # SSB_show = display_signal(fs, N, 2, 1)
    # DSB_show.display_time(modula_SSB, 'DSB signal')
    # DSB_show.display_sprcturm(modula_SSB, 'spectrum of DSB signal')
    plt.show()
