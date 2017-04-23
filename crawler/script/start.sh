#!/bin/bash
WORK_DIR=~/jiafei/zealer/crawler/

cd ${WORK_DIR}

TARGET="zealer.py"
result=`ps -ewf|grep "$TARGET"|grep -wv grep|grep -wv vi | grep -wv tail | grep -wv check_alive | grep -v "\.sh" | grep -v "/alarm " |grep -v "vim"| wc -l `
echo $result

#进程不存在，则告警并重启
NOW_TIME=`date +'%Y-%m-%d %H:%M:%S'`
if [ "$result" -eq "0"  ]
then
    echo "start $TARGET $NOW_TIME" > log/zealer_start.log
    script/kill.sh
    nohup python $TARGET > log/zealer.log 2>&1 &
else
    echo "" #""$TARGET exists $NOW_TIME" >> log/client_down.log
fi

