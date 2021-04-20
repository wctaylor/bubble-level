# main.py
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

import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from .window import BubbleLevelWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.gnome.BubbleLevel',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = BubbleLevelWindow(application=self)
        win.present()

        # Request a proxy for accessing the sensor service.
    #     self.proxy = Gio.DBusProxy.new_for_bus_sync(Gio.BusType.SYSTEM,
    #                                                 Gio.DBusProxyFlags.NONE,
    #                                                 None,
    #                                                 'net.hadess.SensorProxy',
    #                                                 '/net/hadess/SensorProxy',
    #                                                 'net.hadess.SensorProxy',
    #                                                 None)
    #     self.proxy.connect('g-properties-changed',
    #                        window.properties_changed, None)
    #     if self.proxy.get_cached_property('HasAccelerometer'):
    #         self.proxy.call_sync('ClaimAccelerometer', None,
    #                              Gio.DBusCallFlags.NONE, -1, None)

    # def do_shutdown(self):
    #     if self.proxy.get_cached_property('HasAccelerometer'):
    #         self.proxy.call_sync('ReleaseAccelerometer', None,
    #                              Gio.DBusCallFlags.NONE, -1, None)



def main(version):
    app = Application()
    return app.run(sys.argv)
