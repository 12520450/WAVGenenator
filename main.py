import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from scipy.io.wavfile import write
import sounddevice as sd
from mywaveform import generate_waveformAuto, generate_waveformManual, generate_waveformDouble



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
        self.frequency_type = tk.StringVar(value="Ascending")
        self.frequency_step = tk.DoubleVar(value=0)  # 100hz
        self.frequency_sdouble = tk.BooleanVar(value=False)
        self.loop_audio = tk.DoubleVar(value=1)  # Initialize loop_audio
        self.is_playing = tk.DoubleVar(value=1)

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
        
        tk.Label(master, text="Manual Step").grid(row=4, column=0)  
        tk.Entry(master, textvariable=self.frequency_step).grid(row=4, column=1)
        tk.Checkbutton(master, text="(Double)", variable=self.frequency_sdouble).grid(row=4, column=2, columnspan=1)  

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
        sdouble_frequency = self.frequency_sdouble.get()
        frequency_type = self.frequency_type.get()

        if (sdouble_frequency == True):
            scaled_waveform, t, sine_wave, frequencies  = generate_waveformDouble(waveform_type, min_frequency, max_frequency, duration_seconds, 1, frequency_type, 1)
        elif (step_freqeuncy > 0):
            scaled_waveform, t, sine_wave, frequencies  = generate_waveformManual(waveform_type, min_frequency, max_frequency, duration_seconds, 1, frequency_type, 1, step_freqeuncy)
        elif((sdouble_frequency == False) and (step_freqeuncy == 0)): # Auto
            scaled_waveform, t, sine_wave, frequencies  = generate_waveformAuto(waveform_type, min_frequency, max_frequency, duration_seconds, 1, frequency_type, 1)
        else:
            print("to be defined")
            scaled_waveform, t, sine_wave, frequencies  = generate_waveformDouble(waveform_type, min_frequency, max_frequency, duration_seconds, 1, frequency_type, 1)

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
        self.is_playing = 0

    def play_audio(self):
        # while self.loop_audio.get():
        while self.is_playing:
            sd.play(scaled_waveform, self.sampleRate.get())
            sd.wait()
            self.is_playing = self.is_playing - 1

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
