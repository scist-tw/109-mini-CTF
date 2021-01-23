#!/usr/bin/env bash
php output.txt 2>&1 |grep -oP "SCIST{.*}"

