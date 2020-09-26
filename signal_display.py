import matplotlib.pyplot as plt
import numpy as np

class display_signal:
    def __init__(self, t, x=1, y=1):
        plt.figure()
        self.count = 1
        self.t = t
        self.x = x
        self.y = y
    
    def display_time(self, signal, title=''):
        plt.subplot(self.x, self.y, self.count)
        self.count = self.count + 1

        plt.plot(self.t, signal), plt.title(title)

    
    def display_sprcturm(self, signal, title=''):
        signal_fft = np.fft.fft(signal)

        plt.subplot(self.x, self.y, self.count)
        self.count = self.count + 1

        plt.plot(self.t, np.abs(signal_fft)), plt.title(title)

    