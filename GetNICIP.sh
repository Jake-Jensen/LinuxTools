#!/bin/bash

ip -o addr show | awk '$3 == "inet" {print $2, $4}' | cut -d'/' -f1
