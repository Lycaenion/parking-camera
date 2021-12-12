#!/bin/bash

# I've used this to genereate certificates for ssl:
sudo /home/ubuntu/e/bin/certbot certonly \
    --config-dir /home/ubuntu/letsencrypt --logs-dir /tmp/letsencrypt --work-dir /tmp/letsencrypt \
    --standalone \
    -n --agree-tos --email no-reply@aktaotty.com -d aktaotty.com -v

# Then moved them to /etc/nginx/...
