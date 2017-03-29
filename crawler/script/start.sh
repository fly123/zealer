#!/bin/bash
WORK_DIR=~/monitor/alive

cd ${WORK_DIR}

TARGET="client.py luojiafei"
result=`ps -ewf|grep "$TARGET"|grep -wv grep|grep -wv vi | grep -wv tail | grep -wv check_alive | grep -v "\.sh" | grep -v "/alarm " |grep -v "vim"| wc -l `
echo $result

#进程不存在，则告警并重启
NOW_TIME=`date +'%Y-%m-%d %H:%M:%S'`
if [ "$result" -eq "0"  ]
then
    echo "start $TARGET $NOW_TIME" >> log/client_down.log
    script/kill_client.sh
    nohup /usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python $TARGET >> log/client_log.txt 2>&1 &
else
    echo "" #""$TARGET exists $NOW_TIME" >> log/client_down.log
fi

