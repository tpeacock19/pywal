#!/usr/bin/env python
"""
Small Python 3 script to reload GTK3 themes.
"""
import gi
import time

gi.require_version("Gtk", "3.0")
from gi.repository import Gio


def gtk_3_reload():
    """Reload GTK3 themes."""
    settings = Gio.Settings("org.gnome.desktop.interface")
    theme = settings.get_string("gtk-theme")
    settings.set_string("gtk-theme", "")
    time.sleep(1)
    settings.set_string("gtk-theme", theme)


gtk_3_reload()
