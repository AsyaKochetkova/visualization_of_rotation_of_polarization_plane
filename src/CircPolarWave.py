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


class CircularPolarizedWave:
    def __init__(self, amplitude,frequency,side):
        self.amplitude = amplitude  # Амплитуда волны
        self.frequency = frequency    # Частота волны
        self.speed_of_light = 299792458  # Скорость света в вакууме (м/с)
        self.length = self.calculate_wavelength()  # Длина волны
        self.wave_number = 2 * np.pi / self.length  # Волновое число
        self.angular_frequency = 2 * np.pi * self.frequency  # Угловая 
        self.side = side # +1 - right polarized; -1 - left polarized 

    def calculate_wavelength(self):
        return self.speed_of_light/self.frequency     
    
    def y_value(self, position, time):
        return self.amplitude*np.cos(self.angular_frequency*time - self.wave_number*position)
    
    
    def z_value(self,position,time):
        y = self.y_value(position,time)
        return self.side*(-1)*self.amplitude*np.sin(self.angular_frequency*time - self.wave_number*position)