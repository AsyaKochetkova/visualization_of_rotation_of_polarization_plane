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

class LinearlyPolarizedWave:
    def __init__(self,amplitude, frequency, rot_angle=0):
        self.amplitude = amplitude  # Амплитуда волны
        self.frequency = frequency    # Частота волны
        self.speed_of_light = 299792458  # Скорость света в вакууме (м/с)
        self.length = self.calculate_wavelength()  # Длина волны
        self.wave_number = 2 * np.pi / self.length  # Волновое число
        self.angular_frequency = 2 * np.pi * self.frequency  # Угловая 
        self.rot_angle = rot_angle
        self.left_circ_wave = self.calculate_circ_wave(-1)
        self.right_circ_wave = self.calculate_circ_wave(1)

    def calculate_wavelength(self):
        return self.speed_of_light/self.frequency
    
    def calculate_circ_wave(self,direction):
        return CircularPolarizedWave(self.amplitude/2,self.frequency,direction)
    
    def value_in_point_and_time(self, position, time):
        return self.amplitude*np.cos(self.angular_frequency*time - self.wave_number*position)
    
    def modul_value(self, position, time):
        return self.amplitude*np.cos(self.angular_frequency*time - self.wave_number*position)
    
    def y_value(self,position,time):
        return self.value_in_point_and_time(position,time)*np.cos(self.rot_angle)
    
    def z_value(self,position,time):
        return self.value_in_point_and_time(position,time)*np.sin(self.rot_angle)
    
    def change_rot_angle(self,angle):
        self.rot_angle = angle
    