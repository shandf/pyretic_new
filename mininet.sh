#!/bin/bash

sudo ./mn -c
sudo ./mn --custom ./mininet/extra-topos.py --controller remote,port=6633 --mac $@
