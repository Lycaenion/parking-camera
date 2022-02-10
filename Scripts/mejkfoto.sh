#!/bin/bash

LOG_FILE='/home/pi/mejkfoto.log'

{
now=$(date +"%Y_%m_%d %H %M")
IFS=' ' read -r -a splitted <<< "${now}"
datum_part="${splitted[0]}"

hour_part=${splitted[1]}
hour_part_num=`echo ${splitted[1]} | sed 's/^0*//'`

minute_part="${splitted[2]}"

pic_name="${1:-pic_${datum_part}-${hour_part}_${minute_part}.jpg}"
pic_dir="/home/pi/Pictures/ParkingCamera"
pic_path="${pic_dir}/${pic_name}"

if [ "${hour_part_num}" -gt 6 -a "${hour_part_num}" -lt 17 ]; then
    # TODO: use api like:
    # - https://sunrise-sunset.org/api
    # or do it in python using astral:
    # - https://pypi.org/project/astral/1.2/
    echo "It is a day."
    echo "Creating pic ${pic_name}"

    raspistill -ISO 1600 -w 1640 -h 1232 -awb auto -ex auto -o ${pic_path}

    # raspistill -o ${pic_path}
    # raspistill -ISO 1600 -w 1640 -h 1232 -br 80 -co 100 -awb auto -ex auto -o ${pic_path}
    # raspistill -w 1640 -h 1232 -br 80 -co 100 -awb auto -ex auto -o ${pic_path}
else
    echo "It is a night."
    echo "Creating pic ${pic_name}"
    raspistill -w 1640 -h 1232 -br 80 -co 100 -awb auto -ex auto -o ${pic_path}
fi

echo "uploading pic"
curl -v -F "file=@${pic_path}" -- 'http://ec2-3-71-76-8.eu-central-1.compute.amazonaws.com:5000/photos/dooofin'
} 2>&1 1>${LOG_FILE}
