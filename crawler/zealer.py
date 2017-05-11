#encoding=utf-8
import urllib
import time
import json
import my_common
import send_email
import db


import youku
import qq
import sohu
import iqiyi
import le
import acfun
import bilibili
import tudou
import meipai
import youtube
import v1
import pearvideo
import rrmj
import baidu
import a360kan
import toutiao
import zaker
import uc
import yidianzixun
import ttkb
import ifeng
import btime
import shxw
import miaopai
import xiudou


def get_data(channel):
    result_list = []
    if channel == '优酷':
        result_list = youku.main()

    if channel == '腾讯视频':
        result_list = qq.main()

    if channel == '搜狐视频':
        result_list = sohu.main()

    if channel == '爱奇艺':
        result_list = iqiyi.main()

    if channel == '乐视视频':
        result_list = le.main()

    if channel == 'A站':
        result_list = acfun.main()

    if channel == 'B站':
        result_list = bilibili.main()

    if channel == '土豆':
        result_list = tudou.main()

    if channel == '美拍':
        result_list = meipai.main()

    if channel == 'Youtube':
        result_list = youtube.main()

    if channel == '第一视频':
        result_list = v1.main()

    if channel == '梨视频':
        result_list = pearvideo.main()

    if channel == '人人视频':
        result_list = rrmj.main()

    if channel == '百度视频':
        result_list = baidu.main()

    if channel == '360影视':
        result_list = a360kan.main()

    if channel == '今日头条':
        result_list = toutiao.main()

    if channel == 'ZAKER':
        result_list = zaker.main()

    if channel == 'UC':
        result_list = uc.main()

    if channel == '一点资讯':
        result_list = yidianzixun.main()

    if channel == '天天快报':
        result_list = ttkb.main()

    if channel == '凤凰网':
        result_list = ifeng.main()

    if channel == '北京时间':
        result_list = btime.main()

    if channel == '搜狐新闻':
        result_list = shxw.main()

    if channel == '秒拍':
        result_list = miaopai.main()

    if channel == '秀兜':
        result_list = xiudou.main()

    return result_list


def main():
    channel_list = [
            '优酷',
            '腾讯视频',
            '搜狐视频',
            '爱奇艺',
            '乐视视频',
            'A站',
            'B站',
            #'土豆',
            '美拍',
            'Youtube',
            '第一视频',
            # '梨视频',
            '人人视频',
            '百度视频',
            '360影视',
            '今日头条',
            'ZAKER',
            #'UC',
            '一点资讯',
            '天天快报',
            '凤凰网',
            '北京时间',
            '搜狐新闻',
            '秒拍',
            # '秀兜'
        ]

    body_text = ''
    for channel in channel_list:
        try:
            print '********************channel: %s************' % channel
            result_list = get_data(channel)
            print result_list, '\n', len(result_list)

            for result_dict in result_list:
                db.insert_db(result_dict)

        except Exception as e:
            print 'channel: %s   error: %s' % (channel, e)
            if str(e).find('timed out') == -1 and str(e) != '':
                body_text += 'channel: %s   error: %s' % (channel, e)  + '</br>'

    send_email.main(body_text)
    # return result_list


if __name__ == '__main__':
    main()

