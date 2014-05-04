rivalctl
--------

Commandline tool to configure the SteelSeries Rival Gaming Mouse under linux.

Installation
============

    git clone https://github.com/andrepl/rivalctl.git
    sudo python setup.py install

Usage
=====

	usage: rivalctl [-h] [--commit] [--reset] [--wheel-color COLOR]
					[--wheel-style STYLE] [--logo-color COLOR]
					[--logo-style STYLE] [--cpi1 CPI] [--cpi2 CPI]
					[--polling-rate RATE]

	optional arguments:
	  -h, --help           show this help message and exit
	  --commit             Save to firmware
	  --reset              Reset all options to FACTORY defaults
	  --wheel-color COLOR  any valid css color name or hex string
	  --wheel-style STYLE  LED Style [1=Steady, 2-4=Breathe Speed]
	  --logo-color COLOR   any valid css color name or hex string
	  --logo-style STYLE   LED Style [1=Steady, 2-4=Breathe Speed]
	  --cpi1 CPI           50-6500 in increments of 50 [default 800]
	  --cpi2 CPI           50-6500 in increments of 50 [default 1600]
	  --polling-rate RATE  1000, 500, 250, or 125 [default=1000]