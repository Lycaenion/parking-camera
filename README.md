## TODOS
-   delete photos so that last 10 minutes stays undeleted, last hour every 10th minute stays undeleted and last day every hour stays undeleted, last week ...
-   upload photos to local storage, e.g. PC
-   switching camara day mode vs. night mode based on some daylight time different every day...
-   add all files and scripts and system configurations and installations into source code from each device (AWS instance, raspberry, ...)
-   add possibility to manually run clean on from the web page


## Useful commands
-   Clean disc space:
    ```bash
    rm -rf /home/ubuntu/camera/parking-camera/static/photos_uploaded/pic_2022_*_{0,1,2,3,4,5}{1,2,3,4,5,6,7,8,9}.jpg /home/ubuntu/camera/parking-camera/static/thumbs/*
    ```
