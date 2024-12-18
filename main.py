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
from src.WindowGui import Window
import src.Global


'''
wave = LinearlyPolarizedWave(1,600e12)
wave2 = LinearlyPolarizedWave(1,600e12)
quartz_crystal = Material(3,15*np.pi/180)# mm, 
wave2.change_rot_angle(quartz_crystal.get_rotation_angle())
count_point = 100
'''

root = tk.Tk()
app = Window(root)
tk.mainloop()



'''
# Пример использования
if __name__ == "__main__":
    polarization = PolarizationState(angle=30)  # начальный угол поляризации
    material = Material(name='Glass', thickness=10, rotation_factor=0.5)  # свойства материала
    wave = Wave(polarization, material)
    simulation = Simulation(wave)
    simulation.run()


'''