#!/bin/bash
adduser user1
echo 'Added user1...'
adduser user2
echo 'Added user2...'
ifconfig eth0 10.255.6.194 netmask 255.255.255.0 up
route add default gw 10.255.6.5 eth0