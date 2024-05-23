import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data (sine wave)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Compute the FFT
fft_result = np.fft.fft(y)
frequencies = np.fft.fftfreq(len(y))

# Create the sine wave plot
plt.subplot(2, 1, 1)  # Two rows, one column, first subplot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')

# Create the frequency spectrum plot
plt.subplot(2, 1, 2)  # Two rows, one column, second subplot
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')

# Show both plots
plt.tight_layout()  # Adjust spacing between subplots
plt.show()
