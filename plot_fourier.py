from scipy.fftpack import fft
import librosa
import matplotlib.pyplot as plt
import numpy as np


def wav_read(path): # 音声ファイルを読み込む
    wave, fs = librosa.core.load(path, mono=True)
    return wave, fs, path


def calc_fft(data, fs): # FFTする
    frq = np.linspace(0, fs, len(data))
    yf = fft(data)/(len(data)/2)       
    return np.abs(yf), frq

def plot_fourier(source):

    yf = []
    wave, fs, path = wav_read(source)
    yf, frq = calc_fft(wave, fs)

    print(yf)
    sum_yf = sum(yf)

    plt.plot(frq, yf)
    plt.axis([0, fs/2, 0, max(yf)])
    plt.title('Fourier: ' + path)
    plt.xlabel("Frequency(Hz)")
    plt.ylabel("Amplitude")
    plt.show()
    plt.close()
    print('Amplitude Array : ' + str(yf))
    print('Amplitude Sum : ' + str(sum_yf))
    return sum_yf

def calc_snrdb(original, recorded):
    Ps = original
    Pn = recorded
    snr = Ps / Pn
    print('snr : ' + str(snr))
    snr_db = 10 * np.log10(snr)
    print('snr[dB] : ' + str(snr_db))
