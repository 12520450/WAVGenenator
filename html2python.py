import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def generate_waveform(min_frequency, max_frequency, duration, volume, frequency_type,waveform_type, loop):
    sample_rate = 44100  # Adjust as needed
    buffer_size = int(sample_rate * duration)
    t = np.linspace(0, duration, buffer_size, endpoint=False)
    data = np.zeros(buffer_size)

    for i in range(buffer_size):
        current_frequency = min_frequency
        if frequency_type == "ascending":
            current_frequency = min_frequency + ((max_frequency - min_frequency) * (i / buffer_size))
        elif frequency_type == "descending":
            current_frequency = max_frequency - ((max_frequency - min_frequency) * (i / buffer_size))
        elif frequency_type == "random":
            current_frequency = min_frequency + np.random.random() * (max_frequency - min_frequency)

        data[i] = np.sin(2 * np.pi * current_frequency * t[i]) * volume

        if waveform_type == "Sine":
            data[i] = np.sin(2 * np.pi * current_frequency * t[i]) * volume
        elif waveform_type == "Square":
            data[i] = np.sign(np.sin(2 * np.pi * current_frequency * t[i])) * volume
        # elif waveform_type == "Sawtooth":
            
        # elif waveform_type == "Triangle":
        #     # <tbd>
        # else:
        #     print("to be defined!!!")

        # if self.waveform_type.get() == "Sine":
        #     y = self.amplitude.get() * np.sin(2 * np.pi * self.frequency.get() * t)
        # elif self.waveform_type.get() == "Square":
        #     y = self.amplitude.get() * np.sign(np.sin(2 * np.pi * self.frequency.get() * t))
        # elif self.waveform_type.get() == "Sawtooth":
        #     y = self.amplitude.get() * (2 * (self.frequency.get() * t - np.floor(0.5 + self.frequency.get() * t)) - 1)
        # elif self.waveform_type.get() == "Triangle":
        #     y = self.amplitude.get() * np.abs(2 * (self.frequency.get() * t - np.floor(self.frequency.get() * t + 0.5))) - 1
        # else:
        #     print("to be defined!!!")

    if loop:
        data = np.tile(data, int(sample_rate * duration / buffer_size))

    # sd.play(data, sample_rate)

    # # Optional: Display the waveform
    # plt.figure(figsize=(10, 4))
    # plt.plot(t, data[:buffer_size])
    # plt.title("Waveform")
    # plt.xlabel("Time [s]")
    # plt.ylabel("Amplitude")
    # plt.grid()
    # plt.show()
    return t, data

def stop_waveform():
    sd.stop()

# Example usage
# min_frequency = 1
# max_frequency = 2000
# duration = 2
# volume = 0.5
# waveform_type = "ascending"  # Options: "ascending", "descending", "random"
# loop = False

# generate_waveform(min_frequency, max_frequency, duration, volume, waveform_type, loop)


