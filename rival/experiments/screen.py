#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Changes wheel (and logo) color for that one under mouse pointer.
"""

try:
    from rival import open_device
except ImportError:
    import os, sys
    p = os.path.dirname(os.path.realpath(__file__))
    p = os.path.realpath(os.path.join(p, '../'))
    sys.path.insert(0, p)
    from rival import open_device

from gi.repository import Gdk

def get_color_rgb_at(x, y):
    rootwin = Gdk.get_default_root_window()
    pixbuf = Gdk.pixbuf_get_from_window(rootwin, x, y, 1, 1)
    pixels = pixbuf.get_pixels()
    #rowstride = pixbuf.get_rowstride()
    r, g, b = pixels[0], pixels[1], pixels[2]
    color = ord(r), ord(g), ord(b)
    #color = r, g, b
    return color

def get_mouse_pos():
    display = Gdk.Display().get_default()
    dm = Gdk.Display.get_device_manager(display)
    mouse = Gdk.DeviceManager.get_client_pointer(dm)
    screen, x, y = mouse.get_position()
    return x, y

def main():
    while True:
        mousepos = get_mouse_pos()
        pcolor = get_color_rgb_at(*mousepos)
        device = open_device()
        #print(pcolor)
        device.send(device.set_logo_color(pcolor))

if __name__ == "__main__":
    main()
