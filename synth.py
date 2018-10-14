import numpy as np 
from scipy.io.wavfile import write
import matplotlib.pyplot as plt 



class Synth:

    def __init__(self, freq, sps, duration_s):
        self.freq = freq
        self.sps  = sps  #Samples per second
        self.duration_s = duration_s

    def print_info(self):
        print("Frequency:", self.freq)
        print("Samples per second:", self.sps)
        print("Duration:", self.duration_s, "seconds")

    def sine_wave_generator(self, quiet_factor=0.5):
        sample_number = np.arange(self.duration_s * self.sps)
        waveform = np.sinc(np.sin(2 * np.pi * sample_number * self.freq / self.sps))
        waveform_queit = waveform * quiet_factor 
        waveform_integer = np.int16(waveform_queit * (2**32))

        return waveform_integer
    




synth = Synth(440.0, 44100, 5.0)
synth.print_info()
print(synth.sine_wave_generator())