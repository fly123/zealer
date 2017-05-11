#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

#login_url: http://fhh.ifeng.com/index
cookie = 'sid=F47837BD87A29DD7EAD51CE97048168Duser75022317; IF_TIME=1494225871013; IF_USER=media%40zealer.com; IF_REAL=0'


def get_html(url):
    # f = open('ifeng.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['data']['rows']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['pcUrl']
        result_dict['playCount'] = info_dict['pv']
        result_dict['channel'] = '凤凰网'
        result_dict['uploadTime'] = info_dict['submitAuditTime'][: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://fhh.ifeng.com/api/video/videoList?operationStatus=0&pageSize=30&pageNumber=1&_=1491661571555')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

