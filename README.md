RivalCTL
--

**RivalCTL** is an unofficial configuration tool for the SteelSeries Rival Gaming Mouse under linux. This peripheral nor any other product made by SteelSeries, has official Linux support. The tool is limited in it's functionality, since everything had to be reverse-engineered.


Installation
--

Manual Installation:

    git clone https://github.com/pacoqueen/rivalctl.git
    sudo python setup.py install

No Installation:

    cd ~/src/rivalctl/rival
    sudo ./rivalctl.py --logo-color green
    
AUR Package (for Arch Linux):

[rivalctl-git](https://aur.archlinux.org/packages/rivalctl-git/)

Usage
--

    usage: rivalctl [-h] [--commit] [--reset] [--wheel-color COLOR]
                    [--wheel-style STYLE] [--logo-color COLOR]
                    [--logo-style STYLE] [--cpi1 CPI] [--cpi2 CPI]
                    [--profile PROFILE] [--polling-rate RATE]

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
      --profile PROFILE    profile name or path to file
      --polling-rate RATE  1000, 500, 250, or 125 [default=1000]
