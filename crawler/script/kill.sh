#!/bin/bash
ps -ef | grep python | grep monitor.py | grep -v grep | awk '{print $2}' | xargs -i kill -9 {}