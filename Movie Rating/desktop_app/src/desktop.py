# import tkinter as tk
# class ExampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.label = tk.Label(self, text="", width=10)
#         self.label.pack()
#         self.remaining = 0
#         self.countdown(10)
#
#     def countdown(self, remaining = None):
#         if remaining is not None:
#             self.remaining = remaining
#
#         if self.remaining <= 0:
#             self.label.configure(text="time's up!")
#         else:
#             self.label.configure(text="%d" % self.remaining)
#             self.remaining = self.remaining - 1
#             self.after(1000, self.countdown)
#
# if __name__ == "__main__":
#     app = ExampleApp()
#     app.mainloop()
#
#
#
#
# # import tkinter as tk
# #
# # def countdown(self):
# #
# #     self.remaining = 0
# #     self.countdown(10)
# #     if remaining is not None:
# #         self.remaining = remaining
# #
# #     if self.remaining <= 0:
# #         self.label.configure(text="time's up!")
# #     else:
# #         self.label.configure(text="%d" % self.remaining)
# #         self.remaining = self.remaining - 1
# #         self.after(1000, self.countdown)
# #
# # label = tk.Label(text="", width=10)
# # label.pack()
# # rem=2
# # countdown(rem)
#
#
#
#
#
#
#
#
#
#
#
#
# # import tkinter as tk
# #
# # from tktimer import Countdown
# #
# # root = tk.Tk()
# # timer = Countdown(root)
# # timer.grid(row=0, column=0, columnspan=2, sticky="nswe")
# # tk.Button(root, text="Start", command=timer.start).grid(row=1, column=0)
# # tk.Button(root, text="Pause", command=timer.pause).grid(row=1, column=1)
# # root.mainloop()

# import tkinter as tk
# import time
#
# class App():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.label = tk.Label(text="")
#         self.label.pack()
#         self.update_clock()
#         self.root.mainloop()
#
#     def update_clock(self):
#         now = time.strftime("%H:%M:%S")
#         self.label.configure(text=now)
#         self.root.after(1000, self.update_clock)
#
# app=App()




import tkinter as tk
from time import time

class Stopwatch:
    def __init__(self):
        root = tk.Tk()
        root.title('Stopwatch')

        self.display = tk.Label(root, text='00:00', width=20)
        self.display.pack()

        self.button = tk.Button(root, text='Start', command=self.toggle)
        self.button.pack()

        self.paused = True
        root.mainloop()

    def toggle(self):
        if self.paused:
            self.paused = False
            self.button.config(text='Stop')
            self.oldtime = time()
            self.run_timer()
        else:
            self.paused = True
            self.oldtime = time()
            self.button.config(text='Start')

    def run_timer(self):
        if self.paused:
            return
        delta = int(time() - self.oldtime)
        timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
        self.display.config(text=timestr)
        self.display.after(1000, self.run_timer)

Stopwatch()