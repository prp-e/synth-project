import numpy as np 
from scipy.io.wavfile import write
import matplotlib.pyplot as plt 



class Synth:

    def __init__(self, freq, sps, duration_s, quiet_factor):
        self.freq = freq
        self.sps  = sps  #Samples per second
        self.duration_s = duration_s
        self.quiet_factor = quiet_factor

    def print_info(self):
        print("Frequency:", self.freq)
        print("Samples per second:", self.sps)
        print("Duration:", self.duration_s, "seconds")

    def sine_wave_generator(self):
        sample_number = np.arange(self.duration_s * self.sps)
        waveform = np.sinc(np.sin(2 * np.pi * sample_number * self.freq / self.sps))
        waveform_queit = waveform * self.quiet_factor 
        waveform_integer = np.int16(waveform_queit * (2**15))

        return waveform_integer

    def sine_wave_amplitude_modulation(self, modulator_freq):
        pass

    def write_to_file(self, name="synthesizedWave.wav"):
        #to be redefined later. 
       return write(name, self.sps, self.sine_wave_generator())
    




synth = Synth(660.0, 44100, 5.0, 0.8)
synth.print_info()
#print(synth.sine_wave_generator())
synth.write_to_file()