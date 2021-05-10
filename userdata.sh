#!/bin/bash
echo 'Configuring network...'
ifconfig eth0 10.255.6.194 netmask 255.255.255.0 up
route add default gw 10.255.6.5 eth0

echo 'Adding user1...'
adduser user1
mkdir ~/.ssh
echo "key" > /home/user1/.ssh/authorized_keys
chown -R user1:user1 /home/user1/

echo 'Adding user2...'
adduser user2
usermod -aG sudo user2
