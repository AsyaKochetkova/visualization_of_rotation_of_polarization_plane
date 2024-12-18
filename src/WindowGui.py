import tkinter as tk
from tkinter import Frame,Label,Entry,Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import math
from src.CircPolarWave import  CircularPolarizedWave
from src.LinlPolarWave import LinearlyPolarizedWave
from src.Material import Material  # Импорт класса Material
from src.Drawing import Drawing
import src.Global


count_point = 100 

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.wave = LinearlyPolarizedWave(1,600e12)
        self.wave2 = LinearlyPolarizedWave(1,600e12)
        self.quartz_crystal = Material(3,15*np.pi/180)# mm, 
        self.wave2.change_rot_angle(self.quartz_crystal.get_rotation_angle())
        self.v = 0
        self.A = 0
        self.init_window() 

    def Clear(self):      
        print("clear")
        self.textLength.insert(0, "3.0")
        self.textRotSpeed.insert(0, "15.0")  

    def Plot(self):
        self.quartz_crystal.length = float(self.textLength.get())
        self.quartz_crystal.coef = float(self.textRotSpeed.get())  
        self.wave2.change_rot_angle(self.quartz_crystal.get_rotation_angle()) 


    def init_window(self):
        
        wave = self.wave
        c_left_wave = wave.calculate_circ_wave(-1)
        c_right_wave = wave.calculate_circ_wave(1)
        wave2 = self.wave2


        #self.master.title("Use Of FuncAnimation in tkinter based GUI")
        self.pack(fill='both', expand=1)     


        #Create the controls, note use of grid

        self.labelLength = Label(self,text="Length (mm)",width=12)
        self.labelLength.grid(row=0,column=1)
        self.labelRotSpeed = Label(self,text="Rotation coef(deg/mm)",width=12)
        self.labelRotSpeed.grid(row=0,column=2)

        self.textLength = Entry(self,width=12)
        self.textLength.grid(row=1,column=1)
        self.textRotSpeed = Entry(self,width=12)
        self.textRotSpeed.grid(row=1,column=2)

        self.textRotSpeed.insert(0, "15.0")
        self.textLength.insert(0, "3.0")
        self.v = 0
        self.A = 0


        self.buttonPlot = Button(self,text="Plot",command=self.Plot,width=12)        
        self.buttonPlot.grid(row=2,column=1)

        self.buttonClear = Button(self,text="Clear",command=self.Clear,width=12)
        self.buttonClear.grid(row=2,column=2)


        self.buttonClear.bind(lambda e:self.Clear)



        tk.Label(self,text="SHM Simulation").grid(column=0, row=3)


        #tk.Label(self,text="SHM Simulation").grid(column=0, row=3)
        self.fig = plt.Figure(figsize=(8,6))
        self.ax = self.fig.add_subplot(121, projection='3d')
        self.ax.set_ylim3d(-2 * wave.amplitude, 2 * wave.amplitude)
        self.ax.set_zlim3d(-2 * wave.amplitude, 2 * wave.amplitude)

        self.ax2 = self.fig.add_subplot(122, projection='3d')
        self.ax2.set_ylim3d(-2 * wave.amplitude, 2 * wave.amplitude)
        self.ax2.set_zlim3d(-2 * wave.amplitude, 2 * wave.amplitude)

        N = 100
        t=np.linspace(0,1/wave.frequency,N)   
        count_point = 100

        DrawLinWave = Drawing(count_point,wave,0)
        
        y = DrawLinWave.get_y()
        z = DrawLinWave.get_z()
        x = DrawLinWave.get_x()
        self.line1, = self.ax.plot(x, y, z, label='LinWave')

        DrawLeftWave = Drawing(count_point,c_left_wave,0)
        xl,yl,zl = DrawLeftWave.get_x(), DrawLeftWave.get_y(), DrawLeftWave.get_z()
        self.line2, = self.ax.plot(xl,yl,zl, label='LeftWave')

        DrawRightWave = Drawing(count_point,c_right_wave,0)
        xr,yr,zr = DrawRightWave.get_x(), DrawRightWave.get_y(), DrawRightWave.get_z()
        self.line3, = self.ax.plot(xr,yr,zr, label='RightWave')


        self.line4, = self.ax2.plot(x, y, z, label='InitWave')

        DrawFinalWave = Drawing(count_point,wave2,0)
        xf,yf,zf = DrawFinalWave.get_x(), DrawFinalWave.get_y(), DrawFinalWave.get_z()
        self.line5, = self.ax2.plot(xf,yf,zf, label='FinalWave')


        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0,row=4)


        #self.ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, 200), interval=25, blit=False)
        self.ani = FuncAnimation(self.fig, self.update, N, interval=100/N, blit=True)



    def update(self,num):

        wave = self.wave
        c_left_wave = wave.calculate_circ_wave(-1)
        c_right_wave = wave.calculate_circ_wave(1)
        wave2 = self.wave2

        t=np.linspace(0,1/wave.frequency,count_point)

        c_left_wave = wave.calculate_circ_wave(-1)
        c_right_wave = wave.calculate_circ_wave(1)
        i = t[num]

        x,y,z = Drawing(count_point,wave,i).get_x(),Drawing(count_point,wave,i).get_y(),Drawing(count_point,wave,i).get_z()
        xr,yr,zr = Drawing(count_point,c_right_wave,i).get_x(),Drawing(count_point,c_right_wave,i).get_y(),Drawing(count_point,c_right_wave,i).get_z()
        xl,yl,zl = Drawing(count_point,c_left_wave,i).get_x(),Drawing(count_point,c_left_wave,i).get_y(),Drawing(count_point,c_left_wave,i).get_z()
       
        self.line1.set_data_3d(x, y,z)
        self.line2.set_data_3d(xr, yr,zr)
        self.line3.set_data_3d(xl, yl,zl)

        x2,y2,z2 = Drawing(count_point,wave2,i).get_x(),Drawing(count_point,wave2,i).get_y(),Drawing(count_point,wave2,i).get_z()
        self.line4.set_data_3d(x,y,z)
        self.line5.set_data_3d(x2,y2,z2)   

        return self.line1, self.line2, self.line3, self.line4, self.line5,

