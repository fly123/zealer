#encoding=utf-8
import urllib
import time
import json
import common
import HTMLParser


def get_html(url):
    # f = open('bilibili.html')
    # data = f.read()
    # f.close()

    res =urllib.urlopen(url)
    data = res.read()

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data
    info_list = json.loads(data)['data']['vlist']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = 'http://www.bilibili.com/video/av%s/' % info_dict['aid']
        result_dict['playCount'] = info_dict['play']
        result_dict['channel'] = 'B站'
        result_dict['uploadTime'] = common.timestamp_to_str(info_dict['created'])[ : len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://space.bilibili.com/ajax/member/getSubmitVideos?mid=8482768&pagesize=30&tid=0&page=1&keyword=&order=senddate')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

