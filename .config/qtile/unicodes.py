from typing import Optional
from libqtile.widget.textbox import TextBox


def left_half_circle(fg_color):
    return TextBox(
        text='\uE0B6',
        fontsize=20,
        foreground=fg_color,
        padding=0)


def right_powerline_pua(fg_color, bg_color: Optional['str'] = None):
    return TextBox(
        text='\u2771',
        fontsize=25,
        background=bg_color,
        foreground=fg_color,
        padding=4)


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color)


def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=24,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=24,
        background=bg_color,
        foreground=fg_color)
