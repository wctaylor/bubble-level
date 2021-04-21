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

import math
import cairo
from gi.repository import Gtk, Gdk

@Gtk.Template(resource_path='/org/gnome/BubbleLevel/window.ui')
class BubbleLevelWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'BubbleLevelWindow'

    h_area = Gtk.Template.Child()
    v_area = Gtk.Template.Child()
    circle_area = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.h_area.set_size_request(360, 54)
        self.v_area.set_size_request(54, 360)
        self.circle_area.set_size_request(306,306)

        self.h_area.connect("draw", self.on_draw_h)
        self.v_area.connect("draw", self.on_draw_v)
        self.circle_area.connect("draw", self.on_draw_circle)

    # This callback automatically receives the connected drawing area
    # and a Cairo context
    def on_draw_h(self, area, context):
        context.scale(area.get_allocated_width(), area.get_allocated_height())
        context.set_line_width(0.01)

        pattern = cairo.LinearGradient(0, 1, 0, 0)
        pattern.add_color_stop_rgba(0, 1,1,0.5, 1)
        pattern.add_color_stop_rgba(1, 0.2,0.4,0.1, 1)
        context.rectangle(0, 0, 1, 1)
        context.set_source(pattern)
        context.fill()

        context.set_source_rgb(0,0,0)
        context.move_to(0.4, 0)
        context.line_to(0.4, 1)
        context.move_to(0.6, 0)
        context.line_to(0.6, 1)
        context.stroke()
        context.save()

        context.translate(0.5, 0.5)
        context.scale(3/area.get_allocated_width(),
                      2/area.get_allocated_height())
        context.arc(0.0, 0.0, 10, 0.0, 2.0 * math.pi)
        context.restore()
        context.fill()

    # This callback automatically receives the connected drawing area
    # and a Cairo context
    def on_draw_v(self, area, context):
        context.scale(area.get_allocated_width(), area.get_allocated_height())
        context.set_line_width(0.01)

        pattern = cairo.LinearGradient(0, 0, 1, 0)
        pattern.add_color_stop_rgba(0, 1,1,0.5, 1)
        pattern.add_color_stop_rgba(1, 0.2,0.4,0.1, 1)
        context.rectangle(0, 0, 1, 1)
        context.set_source(pattern)
        context.fill()

        context.set_source_rgb(0,0,0)
        context.move_to(0, 0.4)
        context.line_to(1, 0.4)
        context.move_to(0, 0.6)
        context.line_to(1, 0.6)
        context.stroke()
        context.save()

        context.translate(0.5, 0.5)
        context.scale(2/area.get_allocated_width(),
                      3/area.get_allocated_height())
        context.arc(0.0, 0.0, 10, 0.0, 2.0 * math.pi)
        context.restore()
        context.fill()

    # This callback automatically receives the connected drawing area
    # and a Cairo context
    def on_draw_circle(self, area, context):
        context.scale(area.get_allocated_width(), area.get_allocated_height())
        context.set_line_width(0.01)

        pattern = cairo.RadialGradient(0, 0, 0, 0, 0, 1)
        pattern.add_color_stop_rgba(0, 1,1,0.5, 1)
        pattern.add_color_stop_rgba(1, 0.2,0.4,0.1, 1)
        context.arc(0.5, 0.5,
                    0.45, 0.0, 2.0*math.pi)
        context.set_source(pattern)
        context.fill()

        context.set_source_rgb(0,0,0)
        context.move_to(0.05, 0.5)
        context.line_to(0.95, 0.5)
        context.move_to(0.5, 0.05)
        context.line_to(0.5, 0.95)
        context.stroke()

        # context.set_source_rgb(0,0,0)
        context.arc(0.5, 0.5, 0.1, 0.0, 2.0*math.pi)
        context.stroke()
        context.arc(0.5, 0.5, 0.05, 0.0, 2.0*math.pi)
        context.fill()

    def on_property_change(self, proxy, changed, invalidated, user_data):
        print(proxy.get_cached_property('AccelerometerOrientation').get_string())
