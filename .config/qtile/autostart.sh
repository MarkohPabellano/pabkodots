#!/bin/sh

#blueman-applet &
#redshift -l -6.21462:106.84513 &

~/.fehbg &
copyq &
/usr/bin/emacs --daemon &
emacsclient -c -a emacs &
megasync &
syncthing &
nm-applet &
#mictray &
pasystray &
#deadd-notification-center &
picom &
#picom --experimental-backends & ##& disown
/usr/lib/xfce-polkit/xfce-polkit & ##& disown # start polkit agent from xfce
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
