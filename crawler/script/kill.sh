#!/bin/bash
ps -ef | grep python | grep zealer.py | grep -v grep | awk '{print $2}' | xargs -i kill -9 {}
