#!/bin/bash
IFACE=$(/usr/sbin/ifconfig | grep tun0 | awk '{print $1}' | tr -d ':')

if [ "$IFACE" = "tun0" ]; then
    echo "%{F#1bbf3e} %{F#ffffff}$(/usr/sbin/ifconfig | grep tun0 | awk '{print $1}' | tr -d ':')"
else
    echo "%{F#1bbf3e} Disconected"
fi

