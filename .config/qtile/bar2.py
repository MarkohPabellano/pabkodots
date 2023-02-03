from libqtile.bar import Bar


# Widgets Important
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.tasklist import TaskList
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.textbox import TextBox
#from libqtile.widget.image import Image

from colors import gruvbox
from unicodes import left_half_circle, right_powerline_pua

bar = Bar([
    #left_half_circle(gruvbox['yellow']),
    CurrentLayout(background=gruvbox['yellow'],
    ),
    right_powerline_pua(gruvbox['yellow']),

    Spacer(length=10),

    #left_half_circle(gruvbox['dark-blue']),
    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['dark-blue'],
        show_zero=True
    ),
    right_powerline_pua(gruvbox['dark-blue']),

    Spacer(length=10),

    #left_half_circle(gruvbox['cyan']),
    Clock(
        background=gruvbox['cyan'],
        format=' %Y-%m-%d %a %r'),
    right_powerline_pua(gruvbox['cyan']),

    Spacer(length=10),

    # Prompt(foreground=gruvbox['fg']),

    TaskList(
        foreground=gruvbox['fg'],
        icon_size = 1,
        #font = "JetBrainsMono Nerd Font",
        #background
        borderwidth = 2,
        border =gruvbox['blue'],
        margin = 2,
        padding = 0,
        highlight_method = "border",
        title_width_method = "uniform",
        urgent_alert_method = "border",
        urgent_border = '#ffffff',
        rounded = False,
        #txt_floating = "",
        #txt_maximized = "🗖 ",
        #txt_minimized = "",                 
    ),

    Spacer(length=10),

    #left_half_circle(gruvbox['bg']),
    GroupBox(
        disable_drag=True,
        active=gruvbox['dark-cyan'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['magenta'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_powerline_pua(gruvbox['bg']),

    Spacer(length=10),

    Systray(
        padding=15,
        #background='#00000000'
    ),

    Spacer(length=10),

    #left_half_circle(gruvbox['dark-cyan']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['dark-cyan']),
    right_powerline_pua(gruvbox['dark-cyan']),

    Spacer(length=10),

    #left_half_circle(gruvbox['dark-magenta']),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['dark-magenta']),
    right_powerline_pua(gruvbox['dark-magenta']),

    Spacer(length=10),

    #left_half_circle(gruvbox['dark-blue']),
    Net(
        background=gruvbox['dark-blue']
    ),
    right_powerline_pua(gruvbox['dark-blue']),

    #Spacer(length=3),
    
],
    margin=[10, 10, 5, 10],
    background='#00000000',
    opacity=1,
    size=20,
)
