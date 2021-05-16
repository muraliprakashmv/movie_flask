import tkinter as tk
from time import time

root = tk.Tk()
root.title('Stopwatch')
paused = True
global oldtime

def toggle():
    global oldtime
    oldtime = time()
    button.config(text='Start')
    run_timer()

def run_timer():

    delta = int(time() - oldtime)
    timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
    display.config(text=timestr)
    display.after(1000, run_timer)



display = tk.Label(root, text='00:00', width=20)
display.pack()

button = tk.Button(root, text='Start', command=toggle)
button.pack()


root.mainloop()



