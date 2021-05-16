# import tkinter
# import time
# import functools
#
#
# def Timer(func):
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         tic = time.perf_counter()
#         value = func(*args, **kwargs)
#         toc = time.perf_counter()
#         elapsed_time = toc - tic
#         print(f"Elapsed time: {elapsed_time:0.4f} seconds")
#         return value
#     return wrapper_timer
# class simpleapp_tk(tkinter.Tk):
#
#     def __init__(self,parent):
#         tkinter.Tk.__init__(self,parent)
#         self.parent = parent
#         self.initialize()
#
#     def clock(self): # timer tick
#         print("Tick")
#         print("Tick")
#         self.NewTimer = Timer(1, self.clock)
#         self.NewTimer.start()
#
#     def ButtonStartGraphClick(self): # button click
#         self.NewTimer.start()
#
#     def initialize(self): # constructor
#         self.NewTimer = Timer(1,self.clock)
#
# if __name__ == "__main__":
#     app = simpleapp_tk(None)
#     app.geometry("500x250")
#     app.title("TSC")
#     app.mainloop()


try:
    import tkinter as tk
except:
    import Tkinter as tk

import datetime

class App(tk.Frame):
    def __init__(self,master=None,**kw):
        #Create the widgets
        tk.Frame.__init__(self,master=master,**kw)
        self.timeStr = tk.StringVar()
        self.lblTime = tk.Label(self,textvariable=self.timeStr)
        self.lblTime.grid()
        #Call the update function/method to update with current time.
        self.update()

    def update(self):

        self.timeStr.set(datetime.datetime.now().time())
        ## Now use the .after method to call this function again in 1sec.
        self.after(1000,self.update)


if __name__ == '__main__':
    root = tk.Tk()
    App(root).grid()
    root.mainloop()

