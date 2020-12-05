import numpy as np
import matplotlib.pyplot as plt
from modulation import modulation
from signal_display import display_signal
from demodulation import Demodulation

if __name__ == "__main__":
    N = 512  # 采样点数
    fs = 512  # 采样频率
    modula = modulation(fs, N)

    fm = 8  # 调制信号频率
    Am = 2  # 调制信号幅度
    signal_modula = modula.modula_signal(fm, Am)

    fc = 64  # 载波频率
    Ac = 2  # 载波信号幅度
    signal_carried = modula.carried_signal(fc, Ac)

    t_t = np.linspace(0, N / fs, N)  # 时域坐标
    t_s = np.linspace(0, N, N) * fs / N  # 频域坐标

    # 显示调制信号和载波
    signal_show = display_signal(fs, N, 2, 2, title='Raw Signal')
    signal_show.display_time(signal_modula, title='modulated signal')
    signal_show.display_sprcturm(signal_modula, title='specturm of modulated signal')
    signal_show.display_time(signal_carried, title='carried signal')
    signal_show.display_sprcturm(signal_carried, title='specturm of carrried signal')

    # 创建AM信号
    A0 = 2  # 直流偏量，若直流偏量小于调制信号幅度，则会出现“过调幅”现象，无法包络检波
    # modula_AM = modula.Amplitude_Modulation(A0, display_flag=True)  # 常规双边带调制，AM

    # 创建DSB信号
    modula_DSB = modula.DSB_Modulation()   # 抑制载波双边带信号，DSB，全部功率用于信息传输

    # 创建SSB信号
    # 1、滤波法
    # modula_SSB_filter = modula.SSB_Modulation_filter(display_flag=True)
    # 2、相移法
    # modula_SSB_shift = modula.SSB_Modulation_shift(display_flag=True)

    # 信号解调
    Demodulation(fs, N, modula_DSB).Coherent_Demodulation(signal_carried, fm + 3, display_flag=True)

    plt.show()