import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def generate_waveform(min_frequency, max_frequency, duration, volume, waveform_type, loop):
    sample_rate = 44100
    buffer_size = int(sample_rate * duration)
    t = np.linspace(0, duration, buffer_size, endpoint=False)
    data = np.zeros(buffer_size)

    x = 0  # Initialize x (you can choose a different starting value)

    for i in range(buffer_size):
        current_frequency = max_frequency if min_frequency + x > max_frequency else min_frequency + x
        print("current_frequency:", current_frequency)
        # Adjust other parameters (e.g., volume) as needed

        data[i] = np.sin(2 * np.pi * current_frequency * t[i]) * volume

        x += 10  # Increment x by 1 for each iteration

    if loop:
        data = np.tile(data, int(sample_rate * duration / buffer_size))

    sd.play(data, sample_rate)

    # Optional: Display the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(t, data[:buffer_size])
    plt.title("Waveform")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

def stop_waveform():
    sd.stop()

# Example usage
min_frequency = 1
max_frequency = 100
duration = 2
volume = 1
waveform_type = "custom"  # Change to your desired type
loop = False

generate_waveform(min_frequency, max_frequency, duration, volume, waveform_type, loop)
