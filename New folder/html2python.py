import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def write_to_log(message, log_filename='Runtimelog.txt'):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"{message}\n")

def generate_waveform(min_frequency, max_frequency, duration, volume, waveform_type, loop):
    sample_rate = 44100  # Adjust as needed
    buffer_size = int(sample_rate * duration)
    t = np.linspace(0, duration, buffer_size, endpoint=False)
    data = np.zeros(buffer_size)

    current_frequency = min_frequency
    for i in range(buffer_size):
        # current_frequency = min_frequency
        # if waveform_type == "ascending":
        #     current_frequency = min_frequency + ((max_frequency - min_frequency) * (i / buffer_size))
        # elif waveform_type == "descending":
        #     current_frequency = max_frequency - ((max_frequency - min_frequency) * (i / buffer_size))
        # elif waveform_type == "random":
        #     current_frequency = min_frequency + np.random.random() * (max_frequency - min_frequency)

        current_frequency = current_frequency + 1
        if current_frequency == max_frequency:
            current_frequency = max_frequency
        # print("current_frequency: ", current_frequency)

        data[i] = np.sin(2 * np.pi * current_frequency * t[i]) * volume
        # message = current_frequency, "," , data[i]
        # write_to_log("hello")

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
max_frequency = 1000
duration = 1
volume = 1
waveform_type = "ascending"  # Options: "ascending", "descending", "random"
loop = False

generate_waveform(min_frequency, max_frequency, duration, volume, waveform_type, loop)


