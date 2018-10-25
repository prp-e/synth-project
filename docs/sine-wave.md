## Sine Wave
A sine wave or sinusoid is a mathematical curve that describes a smooth periodic oscillation. A sine wave is a continuous wave. It is named after the function sine, of which it is the graph. It occurs often in pure and applied mathematics, as well as physics, engineering, signal processing and many other fields

## How to make a sine wave using synth.py 
To make your own sine wave, you just need to create a new synth object : 

```python 
synth = Synth(frequency, samples_per_second, duration, quiet_factor)
``` 

Then, you can easily use `sine_wave_generator()` method to generate your desired signal. 