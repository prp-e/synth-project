import numpy as np 
from scipy.io.wavfile import write

class Synth:

    def __init__(self, freq, sps, duration_s):
        self.freq = freq
        self.sps  = sps  #Samples per second
        self.duration_s = duration_s

    def print_info(self):
        print("Frequency:", self.freq)
        print("Samples per second:", self.sps)
        print("Duration:", self.duration_s, "seconds")



synth = Synth(440, 44100, 5)
synth.print_info()