#!/bin/bash

find /home/pi/Pictures/ParkingCamera -mmin +120 -exec rm {} \;
