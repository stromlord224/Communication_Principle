import matplotlib.pyplot as plt
import numpy as np
from signal_display import display_signal

class modulation:
    def  __init__(self, N):
        '''
        创建变量t
        @param fs: 采样频率
        '''
        self.N = N
        self.t = np.linspace(-0.01, 0.01, N)
        self.s_m = self.t
        self.s_c = self.t
    
    def modula_signal(self, fm, Am):
        '''
        创建基带调制信号
        @param fm: 载波频率
        @param Am: 载波幅度
        @return: 基带调制信号
        '''
        self.s_m = Am * np.cos(2 * np.pi * fm * self.t)
        return self.s_m

    def carried_signal(self, fc, Ac):
        '''
        创建载波信号
        @param fc: 调制信号频率
        @param Ac: 调制信号幅度
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
        抑制载波双边带信号
        Double Side Band with Suppressed Carrier
        @return: 双边带信号
        """
        s_DSB = self.s_m * self.s_c
        return s_DSB
        


if __name__ == "__main__":
    N = 51200  # 采样点数
    modula = modulation(N)

    fm = 200    # 调制信号频率：200HZ
    Am = 1      # 调制信号幅度
    signal_modula = modula.modula_signal(fm, Am)
    
    fc = 8*fm  # 载波频率：1000HZ
    Ac = 1      # 载波信号幅度
    signal_carried = modula.carried_signal(fc, Ac)
    
    A0 = 2      # 直流偏量
    modula_Am = modula.Amplitude_Modulation(A0)

    signal_modula_fft = np.fft.fft(signal_modula)
    signal_carried_fft = np.fft.fft(signal_carried)
    modula_Am_fft = np.fft.fft(modula_Am)

    t = np.linspace(-0.01, 0.01, N)
    signal_show = display_signal(t, 3, 2)
    signal_show.display_time(signal_modula)
    signal_show.display_sprcturm(signal_modula)
    signal_show.display_time(signal_carried)
    signal_show.display_sprcturm(signal_carried)
    signal_show.display_time(modula_Am)
    signal_show.display_sprcturm(modula_Am)
    plt.show()
