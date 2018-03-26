#!/bin/sh
CURRENT_DIR="$(cd "$(dirname "${0}")" && pwd)"

set -x

COMPOSE_FILE="${1:-docker-compose.yml}"
COMPOSE_FILE="${CURRENT_DIR}/${COMPOSE_FILE}"

cd "${CURRENT_DIR}"
SECS="3"
while :; do
    docker-compose -f "${COMPOSE_FILE}" build && \
    docker-compose -f "${COMPOSE_FILE}" up
    printf "%s\\n" "respawing in ${SECS} secs ..."
    sleep "${SECS}"
done
