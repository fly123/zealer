#encoding=utf-8
import urllib
import time
import json
import my_common
import youku
import qq
import sohu
import iqiyi
import le
import acfun
import bilibili
import tudou
import meipai
import v1
import pearvideo
import rrmj
import a360kan
import toutiao
import uc
import yidianzixun


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

    if channel == '第一视频':
        result_list = v1.main()

    if channel == '梨视频':
        result_list = pearvideo.main()

    if channel == '人人视频':
        result_list = rrmj.main()

    if channel == '360影视':
        result_list = a360kan.main()

    if channel == '今日头条':
        result_list = toutiao.main()

    if channel == 'UC':
        result_list = uc.main()

    if channel == '一点资讯':
        result_list = yidianzixun.main()

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
            '土豆',
            '美拍',
            'Youtube',
            '第一视频',
            '梨视频',
            '人人视频',
            '百度百家号',
            '360影视',
            '今日头条',
            'ZAKER',
            'UC',
            '一点资讯',
            '天天快报',
            '凤凰网',
            '北京时间',
            '搜狐新闻',
            '秒拍'
        ]
    result_list = []
    for channel in channel_list:
        try:
            print '********************channel: %s************' % channel
            rsult_list = get_data(channel)
            print result_list, '\n', len(result_list)
        except Exception as e:
            print 'channel: %s   error: %s' % (channel, e)
    # return result_list


if __name__ == '__main__':
    main()

