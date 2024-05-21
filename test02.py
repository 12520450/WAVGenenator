import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Parameters
duration = 2  # Duration of the sine wave in seconds
frequency = 440  # Frequency of the sine wave in Hz (A4 note)

# Generate the sine wave
t = np.linspace(0, duration, int(duration * 44100), endpoint=False)
sine_wave = np.sin(2 * np.pi * frequency * t)

# Plot the sine wave
plt.plot(t, sine_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.grid(True)
plt.show()

# Play the sine wave
sd.play(sine_wave, 44100)
sd.wait()
