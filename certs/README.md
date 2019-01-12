Self signed certificates
========================

    $ openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -subj /CN=domain.tld                              \
        -keyout privkey.pem -out fullchain.pem
