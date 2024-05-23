# mywaveform
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def write_to_log(message, log_filename='Runtimelog.txt'):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"{message}\n")

def generate_waveform(waveform_type,min_frequency, max_frequency, duration, volume, frequency_type, loop):
    sample_rate = 44100  # Adjust as needed
    buffer_size = int(sample_rate * duration)
    t = np.linspace(0, duration, buffer_size, endpoint=False)
    report_frequency = np.zeros(buffer_size)
    data = np.zeros(buffer_size)

    current_frequency = min_frequency
    for i in range(buffer_size):
        if frequency_type == "Ascending":
            current_frequency = min_frequency + ((max_frequency - min_frequency) * (i / buffer_size))
        elif frequency_type == "Descending":
            current_frequency = max_frequency - ((max_frequency - min_frequency) * (i / buffer_size))
        elif frequency_type == "Keeping":
            current_frequency = current_frequency
        elif frequency_type == "Random":
            current_frequency = min_frequency + np.random.random() * (max_frequency - min_frequency)
        
        report_frequency[i] = current_frequency

        # current_frequency = current_frequency + 1
        # if current_frequency == max_frequency:
        #     current_frequency = max_frequency

        if waveform_type == "Sine":
            data[i] = np.sin(2 * np.pi * current_frequency * t[i]) * volume
        elif waveform_type == "Square":
            data[i] = np.sign(np.sin(2 * np.pi * current_frequency * t[i]))*volume
        elif waveform_type == "Sawtooth":
            data[i] = volume * (2 * (current_frequency * t[i] - np.floor(0.5 + current_frequency * t[i])) - 1)
        elif waveform_type == "Triangle":
            data[i] = volume * np.abs(2 * (current_frequency * t[i] - np.floor(current_frequency * t[i] + 0.5))) - 1
        else:
            print("to be defined!!!")

    if loop > 1:
        data = np.tile(data, int(sample_rate * duration / buffer_size))

    # Scale the waveform to 16-bit PCM format
    scaled_waveform = np.int16(data * 32767)

    return scaled_waveform, t, data, report_frequency