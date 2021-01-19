#!/bin/sh
docker-compose down
chmod 777 ./Manager/src/upload
docker-compose up -d
