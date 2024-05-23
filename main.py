import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from scipy.io.wavfile import write
import sounddevice as sd
from mywaveform import generate_waveform


def calcuated_numsamples(min_frequency, max_frequency, step):
    try:
        num_samples = ((max_frequency - min_frequency)// step)
    except:
        print("Something went wrong when calcuated_numsamples()")

    return num_samples

class WaveformGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Waveform Generator")
        self.amplitude = tk.DoubleVar(value=10)
        self.frequency = tk.DoubleVar(value=500)
        self.min_frequency = tk.DoubleVar(value=1)
        self.max_frequency = tk.DoubleVar(value=2000)
        self.sampleRate = tk.DoubleVar(value=44100)  # Adjust as needed
        self.duration = tk.DoubleVar(value=1)  # 5s
        self.waveform_type = tk.StringVar(value="Sine")
        self.frequency_type = tk.StringVar(value="ascending")
        self.frequency_step = tk.DoubleVar(value=100)  # 100hz
        self.frequency_sdouble = tk.BooleanVar(value=False)
        self.loop_audio = tk.DoubleVar(value=1)  # Initialize loop_audio
        self.is_playing = False

        tk.Label(master, text="SampleRate*").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.sampleRate).grid(row=0, column=1)

        tk.Label(master, text="Amplitude*").grid(row=1, column=0)  
        tk.Entry(master, textvariable=self.amplitude).grid(row=1, column=1)  

        tk.Label(master, text="Frequency*").grid(row=2, column=0)
        tk.Entry(master, textvariable=self.frequency).grid(row=2, column=1)

        tk.Label(master, text="Min*").grid(row=3, column=0)
        tk.Entry(master, textvariable=self.min_frequency).grid(row=3, column=1)
        tk.Label(master, text="Max*").grid(row=3, column=2)
        tk.Entry(master, textvariable=self.max_frequency).grid(row=3, column=3)
        
        tk.Label(master, text="Step up/down").grid(row=4, column=0)  
        tk.Entry(master, textvariable=self.frequency_step).grid(row=4, column=1)
        tk.Checkbutton(master, text="(Step double)", variable=self.frequency_sdouble).grid(row=4, column=2, columnspan=1)  

        tk.Label(master, text="Frequency type*").grid(row=5, column=0)  
        tk.OptionMenu(master, self.frequency_type, "Ascending", "Descending","Keeping","Random").grid(row=5, column=1, columnspan=2)  
        
        tk.Label(master, text="Waveform Type*").grid(row=6, column=0)  
        tk.OptionMenu(master, self.waveform_type, "Sine", "Square", "Sawtooth", "Triangle").grid(row=6, column=1, columnspan=2)


        # Create a button to review
        # tk.Label(master, text="Duration:").grid(row=5, column=0)
        # tk.Entry(master, textvariable=self.duration).grid(row=5, column=1)
        tk.Button(master, text="(Review)", command=self.review).grid(row=7, column=0, columnspan=2)

        # Create a button to start/stop the loop
        tk.Label(master, text="Loop").grid(row=7, column=1)
        tk.Entry(master, textvariable=self.loop_audio).grid(row=7, column=2)
        tk.Button(master, text="Play", command=self.start_audio).grid(row=7, column=3, columnspan=1)
        tk.Button(master, text="Stop", command=self.stop_audio).grid(row=7, column=4, columnspan=1)
        
    
    # To display the wave chart before start playing
    def review(self):
        self.execute01()

    def execute01(self):
        global scaled_waveform
        waveform_type = self.waveform_type.get()
        duration_seconds = self.duration.get()
        min_frequency = self.min_frequency.get()
        max_frequency =  self.max_frequency.get()
        step_freqeuncy = self.frequency_step.get()
        frequency_type = self.frequency_type.get()


        # num_samples = int(self.sampleRate.get() * duration_seconds)
        # t = np.linspace(0, duration_seconds, num_samples)  # Adjust time array
        # y = np.zeros(num_samples)

        # # if self.frequency_type.get() == "ascending":
        # timecount = calcuated_numsamples(min_frequency, max_frequency, step_freqeuncy)
        # print("num_samples: ", num_samples)
        # updated_frequency = np.linspace(min_frequency, max_frequency, int(timecount)+1)
        # print("updated_frequency: ", updated_frequency)
        
        # for i in range(num_samples):
        #     # frequency = min_frequency + ((max_frequency - min_frequency) * (i / num_samples))
            
        #     # Map i to the nearest multiple of int(timecount)
        #     frequency = int(i // (int(timecount)+1)) * (int(timecount)+1)
        #     print("int(timecount): ", int(timecount))
        #     print("frequency: ", frequency)
        #     if self.waveform_type.get() == "Sine":
        #         y[i] = self.amplitude.get() * np.sin(2 * np.pi * frequency * t[i])
        #     # elif self.waveform_type.get() == "Square":
        #     #     y += self.amplitude.get() * np.sign(np.sin(2 * np.pi * frequency * t))
        #     # elif self.waveform_type.get() == "Sawtooth":
        #     #     y += self.amplitude.get() * (2 * (frequency * t - np.floor(0.5 + frequency * t)) - 1)
        #     # elif self.waveform_type.get() == "Triangle":
        #     #     y += self.amplitude.get() * np.abs(2 * (frequency * t - np.floor(frequency * t + 0.5))) - 1
        #     # else:
        #     #     raise ValueError(f"Unknown waveform type: {self.waveform_type.get()}")
            
        #     # print("i:", i, "frequency:", frequency)

        scaled_waveform, t, sine_wave, frequencies  = generate_waveform(waveform_type, min_frequency, max_frequency, duration_seconds, 1, frequency_type, 1)

        # Create the sine wave plot
        plt.clf()
        plt.subplot(2, 1, 1)  # Two rows, one column, first subplot
        plt.plot(t, sine_wave)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title(f'Waveform Review (Frequency = {int(min_frequency)} : {int(max_frequency)} Hz )')

        # Create the frequency spectrum plot
        plt.subplot(2, 1, 2)  # Two rows, one column, second subplot
        plt.plot(t, frequencies)
        plt.xlabel('Time')
        plt.ylabel('Frequency (Hz)')
        plt.title('Frequency Spectrum')

        # Show both plots
        plt.tight_layout()  # Adjust spacing between subplots
        plt.show()
    
    def stop_audio(self):
        sd.stop()
        # Stop the loop_audio flag
        # self.loop_audio.set(False)
        self.is_playing = False

    def play_audio(self):
        # while self.loop_audio.get():
        while self.is_playing:
            sd.play(scaled_waveform, self.sampleRate.get())
            sd.wait()

    def start_audio(self):
        self.execute01()
        sd.play(scaled_waveform, self.sampleRate.get())

        # if self.loop_audio.get():
        self.is_playing = self.loop_audio.get()
        if self.is_playing:
            # Start a separate thread or asynchronous task for looping playback
            import threading
            loop_thread = threading.Thread(target=self.play_audio)
            loop_thread.start()

            # Store the loop_thread reference (e.g., as an instance variable)
            self.loop_thread = loop_thread


root = tk.Tk()
app = WaveformGenerator(root)
root.mainloop()
