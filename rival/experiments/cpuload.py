#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Changes wheel (and logo) color acording to CPU load.
"""

import psutil

try:
    from rival import open_device
except ImportError:
    import os, sys
    p = os.path.dirname(os.path.realpath(__file__))
    p = os.path.realpath(os.path.join(p, '../'))
    sys.path.insert(0, p)
    from rival import open_device

def get_cpuload():
    """
    Blocking. Returns CPU load as a percentage 0..100.
    """
    res = psutil.cpu_percent(1)     # 1 second interval
    return res

def get_color_from(cpuload):
    """
    Transfonr a percentage to a color.
    """
    r = round(cpuload * 255.0 / 100)
    g = 255 - round(cpuload * 255.0 / 100)
    return (r, g, 0)

def main():
    while True:
        cpuload = get_cpuload()
        color = get_color_from(cpuload)
        device = open_device()
        device.send(device.set_logo_color(color))

if __name__ == "__main__":
    main()
