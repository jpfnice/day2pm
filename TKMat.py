

import tkinter as tk 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np



class MyWindow(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self) # <=> super().__init__()
        
        self.minsize(600,200)
        self.title("Just a test")
        
       # self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
#        self.rowconfigure(0, weight=1)
#         self.rowconfigure(1, weight=1)

        # Binding variables:
        self.miniVal=tk.IntVar()
        self.maxiVal=tk.IntVar()
        self.totalVal=tk.IntVar()
       
        mini=tk.Entry(self, textvariable=self.miniVal)
        mini.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E+tk.W)
        maxi=tk.Entry(self, textvariable=self.maxiVal)
        maxi.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E+tk.W)
        total=tk.Entry(self, textvariable=self.totalVal)
        total.grid(row=0, column=2, padx=10, pady=10, sticky=tk.E+tk.W)
        
        update=tk.Button(self, text="Update", command=self.update)
        update.grid(row=0, column=3, padx=10, pady=10, sticky=tk.E+tk.W)
        
        fig = plt.Figure(figsize=(3, 2), dpi=300)
        self.axe=fig.add_subplot(111)
        
        x=np.linspace(-10,10,300)

        y=np.sin(x)
        y2=np.cos(x)

        self.axe.plot(x, y, label="sin")
        self.axe.plot(x, y2, label="cos")
        
        self.canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget()
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky=tk.E+tk.W)
    
    def update(self): 
        x=np.linspace(self.miniVal.get(),self.maxiVal.get(),self.totalVal.get())
        y=np.sin(x)
        y2=np.cos(x)
        self.axe.plot(x, y, label="sin")
        self.axe.plot(x, y2, label="cos")
        self.canvas.draw()
              
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()
