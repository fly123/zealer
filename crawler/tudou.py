#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


def get_html(url):
    # f = open('tudou.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['data']['data']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = 'http://www.tudou.com/programs/view/%s/' % info_dict['code']
        result_dict['playCount'] = info_dict['playNum']
        result_dict['channel'] = '土豆'
        result_dict['uploadTime'] = my_common.timestamp_to_str(info_dict['pubDate'] / 1000)[: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://www.tudou.com/home/item/list.do?uid=101421847&page=1&pageSize=40&sort=1&keyword=')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

