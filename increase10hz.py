import numpy as np
import matplotlib.pyplot as plt

# Parameters
min_frequency = 0  # Minimum frequency in Hz
max_frequency = 100  # Maximum frequency in Hz
duration = 10       # Duration of the signal in seconds
sampling_rate = 44100  # Sampling rate (samples per second)

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the sine wave with increasing frequency
frequency_range = np.arange(min_frequency, max_frequency + 10, 10)
sine_wave = np.zeros(len(t))

for freq in frequency_range:
    sine_wave += np.sin(2 * np.pi * freq * t)

# Normalize the amplitude
sine_wave /= len(frequency_range)

# Plot the resulting sine wave
plt.figure(figsize=(8, 4))
plt.plot(t, sine_wave, label="Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave with Increasing Frequency")
plt.grid(True)
plt.legend()
plt.show()
