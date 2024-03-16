#!/bin/bash

# Si da error en esta interfaz, agregarla manualmente
interface=$(/usr/sbin/ifconfig -s | head -n 2 | tail -n 1 | awk '{print $1}')

echo "%{F#2495e7}󰈀 %{F#ffffff}$(/usr/sbin/ifconfig $interface | grep 'inet ' | awk '{print $2}')"