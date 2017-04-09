#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


def get_html(url):
    # f = open('zaker.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, '', ' ')

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['rows']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['url']
        result_dict['playCount'] = info_dict['pv']
        result_dict['channel'] = 'ZAKER'
        result_dict['uploadTime'] = my_common.timestamp_to_str(info_dict['modified'])[: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://cms.myzaker.com/index.php?cpeditor/article/articles/&superaction=&app_id=11837&stat=&keyword=&author=&position=&startdate=&enddate=')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

