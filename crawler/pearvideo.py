#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

cookie = 'JSESSIONID=038C0E6A517B4D0C382AA70AC123EA80; PV_CMS=srv-pv-prod-cms1_80'


def get_html(url, post_data):
    # f = open('pearvideo.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie, post_data)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['rows']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['name']
        result_dict['link'] = 'http://www.pearvideo.com/video_%s' % info_dict['content_id']
        result_dict['playCount'] = info_dict['total_site_pv']
        result_dict['channel'] = '梨视频'
        result_dict['uploadTime'] = info_dict['first_publish_t'][ : len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url, post_data):
    result_list = []

    html = get_html(url, post_data)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    post_data = '_search=false&nd=1490692042733&rows=50&page=1&sidx=&sord=asc&tableType=5&nodeId=123'
    result_list = get_data('http://139.224.6.185/cms-admin/report/queryNewContentStatList.json', post_data)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

