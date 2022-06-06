import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

def make_wave(frequency, time=3):
    a = 0.1
    f0 = frequency
    fs = 44100
    sec = time

    filename = str(frequency) + 'Hz_Sin.wav'

    n = np.arange(fs * sec)
    s = a * np.sin(2.0 * np.pi * f0 * n / fs)

    plt.plot(s[:int(fs/f0)])
    plt.show()

    s = [int(x * 32767.0) for x in s]

    bin = struct.pack('h' * len(s), *s)

    w = wave.Wave_write(filename)
    p = (1, 2, fs, len(bin), 'NONE', 'not compressed')
    w.setparams(p)
    w.writeframes(bin)
    w.close()