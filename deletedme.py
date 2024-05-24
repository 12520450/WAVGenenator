import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(text="0")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.start_button = tk.Button(text="Start", command=self.start)
        self.start_button.pack()

    def start(self):
        self.counter = int(self.entry.get())
        self.root.after(1000, self.update_counter)

    def update_counter(self):
        self.counter -= 1
        # self.label.config(text=str(self.counter))
        if self.counter > 0:
            self.root.after(1000, self.update_counter)

root = tk.Tk()
app = App(root)
root.mainloop()
