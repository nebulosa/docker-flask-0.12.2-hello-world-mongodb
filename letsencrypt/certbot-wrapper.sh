#!/bin/sh

while :; do
    printf "%s\\n" "Attempting to secure https://${APP_DOMAIN}"

    if  certbot renew --dry-run | grep -q "No renewals were attempted"; then
        if certbot certonly --webroot --register-unsafely-without-email --agree-tos \
            -w /etc/letsencrypt/challenge -d "${APP_DOMAIN}"; then

            cp /etc/letsencrypt/live/${APP_DOMAIN}/*.pem /etc/letsencrypt/certs/
            printf "%s\\n" "Certs updated, reload nginx to apply modifications:"
            printf "%s\\n" "$ docker-compose -f docker-compose.yml kill -s SIGHUP nginx"
        fi

    else
        certbot renew
    fi

    sleep 24h
done
