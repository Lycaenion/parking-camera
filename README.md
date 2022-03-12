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

-   Permanently output system logs (and show last 100 lines):
    ```bash
    sudo tail -f -n 100 /var/log/syslog
    ```

-   Reload systemctl configurations, useful after updating systemd,
    configuration file:
    ```bash
    sudo systemctl daemon-reload
    ```

-   Restart uwsgi systemd service:
    ```bash
    sudo systemctl restart aktaotty.service
    ```

-   Show status of aktaotty service:
    ```bash
    sudo systemctl status aktaotty.service
    ```

-   Show used ports:
    ```bash
    sudo lsof -i -P -n | grep LISTEN
    ```

-   Allow port 5000 on firewall:
    ```bash
    sudo ufw allow 5000
    ```

-   Generate https certificates:
    ```bash
    sudo /home/ubuntu/e/bin/certbot certonly --standalone -n --agree-tos --email no-reply@aktaotty.com -d aktaotty.com --config-dir /home/ubuntu/letsencrypt --logs-dir /tmp/letsencrypt --work-dir /tmp/letsencrypt -v
    ```
    Find correct ones:
    ```bash
    sudo ls -la /home/ubuntu/letsencrypt/live/aktaotty.com/
    ```
    Then copy them to proper place:
    ```bash
    cp /home/ubuntu/letsencrypt/archive/aktaotty.com/fullchain2.pem /etc/nginx/ssl/aktaotty.com.crt
    cp /home/ubuntu/letsencrypt/archive/aktaotty.com/privkey2.pem /etc/nginx/ssl/aktaotty.com.key
    ```
    Then restart nginx:
    ```bash
    sudo systemctl restart nginx
    ```

-   Show current public IP, when on AWS EC2 instance:
    ```bash
    TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
    curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/public-ipv4
    ```

-   Install necessary system packages:
    ```bash
    sudo apt install python3 python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev python3-setuptools nginx curl wget jq vim screen git
    ```

-   Create python virtual environment (e):
    ```bash
    python3 -m venv e
    ```

-   Activate python virtual environment (e):
    ```bash
    . e/bin/activate
    ```

-   Install necessary python packages:
    ```bash
    pip install -U pip
    pip install -r requirements.txt
    ```

-   Manually run application:
    ```bash
    export FLASK_ENV=development
    flask run --host=0.0.0.0
    ```

-   Setup git:
    ```bash
    git config --global user.email "<user.name>@example.com"
    git config --global user.name Lycaenion
    git config --global core.editor "vim"
    git config credential.helper 'cache --timeout=300'
    ```
