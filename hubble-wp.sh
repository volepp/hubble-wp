#!/bin/bash
PID=$(pgrep gnome-session | tail -n1)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

/usr/bin/python /home/oliver/hubble-wp/hubble_wp.py
