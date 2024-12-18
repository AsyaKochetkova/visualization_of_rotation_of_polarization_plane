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


class Drawing:
    def __init__(self, count_point, wave, t):
        self.y = np.empty(count_point)
        self.z = np.empty(count_point)
        self.x = np.linspace(0, 3*wave.length, count_point)
        k = 0

        for x in self.x:
            self.y[k] = wave.y_value(x,t)
            self.z[k] = wave.z_value(x,t)
            k += 1

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z        

    