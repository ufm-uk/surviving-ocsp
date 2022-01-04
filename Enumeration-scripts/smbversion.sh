#!/bin/sh
#Author: lee carter
#Description:
# Requires root or enough permissions to use tcpdump
# Hope this helps someone :)
if [ -z $1 ]; then echo "Usage: ./smbversion.sh RHOST INTERFACE {RPORT}" && exit; else rhost=$1; fi
if [ ! -z $3 ]; then rport=$3; else rport=139; fi
if [ ! -z $2 ]; then interface=$2; else interface=tun0; fi
tcpdump -s0 -n -i $interface src $rhost and port $rport -A -c 7 2>/dev/null | grep -i "samba\|s.a.m" | tr -d '.' | grep -oP 'UnixSamba.*[0-9a-z]' | tr -d '\n' & echo -n "$rhost: " &
echo "exit" | smbclient -L $rhost 1>/dev/null 2>/dev/null
echo "" && sleep .1

