#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

cookie = 'JSESSIONID=79518463F23EBE56202ABF183290D4EC'


def get_html(url, post_data):
    # f = open('rrmj.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie, post_data)

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data
    info_list = json.loads(data)['data']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = 'https://mobile.rr.tv/pages/videoShare/?id=%s' % info_dict['id']
        result_dict['playCount'] = info_dict['playCount']
        result_dict['channel'] = '人人视频'
        result_dict['uploadTime'] = my_common.timestamp_to_str(info_dict['updateTime'] / 1000)[: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url, post_data):
    result_list = []

    html = get_html(url, post_data)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    post_data = 'userId=10233732&title=&videoStatusType=pass&isDel=false&page=1&rows=30'
    result_list = get_data('http://ucenter.rrmj.tv/video/myVideo', post_data)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

