import numpy as np 
from scipy.io.wavfile import write
import matplotlib.pyplot as plt 



class Synth:

    def __init__(self, freq, sps, duration_s, quiet_factor=0.8):
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
        waveform = np.sin(2 * np.pi * sample_number * self.freq / self.sps)
        waveform_quiet = waveform * self.quiet_factor 
        #waveform_integer = np.int16(waveform_queit * (2**15))

        return waveform_quiet

    def sine_wave_amplitude_modulation(self, modulator_freq=0.25, ac=1.0, ka=0.25):
        t_samples = np.arange(self.sps * self.duration_s)
        modulator = np.sin(2 * np.pi * t_samples * modulator_freq / self.sps) 
        envelope = ac * (1.0 + ka * modulator)
        modulated_signal = self.sine_wave_generator() * envelope 

        return modulated_signal

    def square_wave_generator(self):
        sample_number = np.arange(self.duration_s * self.sps)
        waveform = np.sign(np.sin(self.freq * sample_number)) 
        waveform_quiet = waveform * self.quiet_factor

        return waveform_quiet

    def write_to_file(self, default_method, name="synthesizedWave.wav"):
        #to be redefined later. 
        return write(name, self.sps, default_method)
    




synth = Synth(440.0, 44100, 5.0)
synth.print_info()
#print(synth.sine_wave_generator())
synth.write_to_file(synth.sine_wave_generator(), "Sine.wav")
synth.write_to_file(synth.square_wave_generator(), "Square.wav")