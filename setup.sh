#!/bin/sh
CURRENT_DIR="$(cd "$(dirname "${0}")" && pwd)"

PS4="> "; set -xe

cd "${CURRENT_DIR}"
SECS="3"; while :; do
    docker-compose build
    docker-compose up
    printf "%s\\n" "respawing in ${SECS} secs ..."
    sleep "${SECS}"
done
