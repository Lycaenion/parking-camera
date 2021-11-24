#!/bin/bash

pic_name=pic_$(date +"%Y%m%d_%H%M%S").jpg
pic_dir="/home/pi/Pictures/ParkingCamera"
pic_path="${pic_dir}/{${pic_name}"

echo "Creating pic ${pic_name}"
raspistill -o ${pic_path}

echo "Uploading pic"
curl -v -F "file=@${pic_path}" -- 'http://ec2-3-123-28-220.eu-central-1.compute.amazonaws.com:5000/photos/doofin'
