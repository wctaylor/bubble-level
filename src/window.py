# window.py
#
# Copyright 2021 Will Taylor
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


import numpy as np
from matplotlib.figure import Figure
from matplotlib.patches import Circle, Ellipse
from matplotlib.backends.backend_gtk3cairo import (FigureCanvasGTK3Cairo
                                                   as FigureCanvas)

@Gtk.Template(resource_path='/org/gnome/BubbleLevel/window.ui')
class BubbleLevelWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'BubbleLevelWindow'

    h_container       = Gtk.Template.Child()
    v_container       = Gtk.Template.Child()
    circle_container  = Gtk.Template.Child()
    dpi = 282.45

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plot_horizontal_bubble()
        self.plot_vertical_bubble()
        self.plot_circle_bubble()

    def plot_horizontal_bubble(self):
        fig = Figure(figsize=(360/self.dpi, 108/self.dpi), dpi=self.dpi,
                     frameon=False)
        ax = fig.add_subplot()
        canvas = FigureCanvas(fig)
        canvas.set_size_request(360, 108)


        center = (0.5, 0.10)
        bubble = Ellipse(xy=center, width=0.25, height=0.15, angle=0)
        ax.set(xlim=(0, 1), ylim=(0, 0.2))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axvline(x=0.35, color='black', linewidth=0.4)
        ax.axvline(x=0.65, color='black', linewidth=0.4)
        ax.add_patch(bubble)

        canvas.show()
        self.h_container.add(canvas)

    def plot_vertical_bubble(self):
        fig = Figure(figsize=(108/self.dpi, 360/self.dpi), dpi=self.dpi,
                     frameon=False)
        ax = fig.add_subplot()
        canvas = FigureCanvas(fig)
        canvas.set_size_request(108, 360)


        center = (0.1, 0.5)
        bubble = Ellipse(xy=center, width=0.15, height=0.25, angle=0)
        ax.set(xlim=(0, 0.2), ylim=(0, 1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axhline(y=0.35, color='black', linewidth=0.4)
        ax.axhline(y=0.65, color='black', linewidth=0.4)
        ax.add_patch(bubble)

        canvas.show()
        self.v_container.add(canvas)

    def plot_circle_bubble(self):
        fig = Figure(figsize=(252/self.dpi, 252/self.dpi), dpi=self.dpi,
                     frameon=False)
        ax = fig.add_subplot()
        canvas = FigureCanvas(fig)
        canvas.set_size_request(252, 252)

        center = (0.5, 0.5)
        bubble = Circle(xy=center, radius=0.1)
        guide  = Circle(xy=center, radius=0.15, fill=False, color='black')
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axhline(y=0.5, color='black', linewidth=0.4)
        ax.axvline(x=0.5, color='black', linewidth=0.4)
        ax.add_patch(bubble)
        ax.add_patch(guide)

        canvas.show()
        self.circle_container.add(canvas)

