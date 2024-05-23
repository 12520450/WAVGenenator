import matplotlib.pyplot as plt
import numpy as np

def display(x, y, frequency):
    """
    Calculate the product of two inputs and display the frequency spectrum.

    Parameters
    ----------
    x : float or array-like
        First input value(s).
    y : float or array-like
        Second input value(s).
    frequency : float
        Frequency value for the sine wave.

    Returns
    -------
    z : float or array-like
        Product of x and y.
    """
    # Compute the product of x and y
    z = x * y

    # Generate some sample data (sine wave)
    t = np.linspace(0, 2 * np.pi, 100)
    sine_wave = np.sin(2 * np.pi * frequency * t)

    # Create the sine wave plot
    plt.subplot(2, 1, 1)  # Two rows, one column, first subplot
    plt.plot(t, sine_wave)
    plt.xlabel('Time')
    plt.ylabel('sin(2πft)')
    plt.title(f'Sine Wave (Frequency = {frequency} Hz)')

    # Create the frequency spectrum plot
    plt.subplot(2, 1, 2)  # Two rows, one column, second subplot
    fft_result = np.fft.fft(sine_wave)
    frequencies = np.fft.fftfreq(len(sine_wave))
    plt.plot(frequencies, np.abs(fft_result))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum')

    # Show both plots
    plt.tight_layout()  # Adjust spacing between subplots
    plt.show()

    return z

    print(f"Product of {x_value} and {y_value} = {product_result}")

# Example usage
x_value = 0.7
y_value = 25.4
freq_value = 5.0  # Set your desired frequency here
product_result = display(x_value, y_value, freq_value)

