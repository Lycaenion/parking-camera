#!/bin/bash

pic_name=${1:-pic_$(date +"%Y%m%d_%H%M%S").jpg}

pics_dir_remote="/home/pi/Pictures"
pic_path_remote="${pics_dir_remote}/${pic_name}"
remote_host="192.168.0.187"

echo "Creating pic ${pic_path_remote}"
ssh pi@${remote_host} "raspistill -o ${pic_path_remote}"

echo "Copying pic ${pic_path_remote}"
scp pi@${remote_host}:${pic_path_remote} ./${pic_name}

curl -v -F "file=@${pic_name}" -- 'http://ec2-3-123-28-220.eu-central-1.compute.amazonaws.com:5000/photos/dooofin'
