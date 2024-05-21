import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], lw=2)

# Set the axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x + frame * 0.1)  # Adjust the frequency increment here
    line.set_data(x, y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True)

# Show the plot
plt.title("Real-Time Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
