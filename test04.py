import numpy as np

def execute01(self):
    global scaled_waveform
    duration_seconds = self.duration.get()
    num_samples = int(self.sampleRate.get() * duration_seconds)
    t = np.linspace(0, duration_seconds, num_samples)  # Adjust time array

    min_freq = 1  # Minimum frequency (in Hz)
    max_freq = 10  # Maximum frequency (in Hz)

    # Create an empty array to store the waveform
    y = np.zeros(num_samples)

    # Generate the waveform with ascending frequencies
    for freq in range(min_freq, max_freq + 1):
        y += self.amplitude.get() * np.sin(2 * np.pi * freq * t)

    # Store the resulting waveform (y) in scaled_waveform or use it as needed
    scaled_waveform = y

# Call the modified function
execute01(self)