#!/bin/bash

# Extract unique IPs from SSH connection attempts in the log
IP_LIST=$(grep "sshd" /var/log/auth.log | grep -oP '(?<=from )\d{1,3}(\.\d{1,3}){3}' | sort -u | tail -20)

# Loop through the IPs and get their geolocation
echo "IP Address - Geolocation:"
echo "--------------------------"

for IP in $IP_LIST
do
    LOCATION=$(geoiplookup $IP | awk -F ": " '{print $2}')
    echo "$IP - $LOCATION"
done
