#encoding=utf-8
import urllib
import time
import json
import common
import HTMLParser


def get_html(url):
    # f = open('le.html')
    # data = f.read()
    # f.close()

    res =urllib.urlopen(url)
    data = res.read()

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data

    data = data[len('jQuery191016755304000198934_1490429838177(') : -1]
    info_list = json.loads(data)['data']['list']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = 'http://www.le.com/ptv/vplay/%s.html' % info_dict['vid']
        result_dict['playCount'] = info_dict['hits']
        result_dict['channel'] = '乐视视频'

        uploadTime = info_dict['uploadTime']
        # print uploadTime
        uploadTime = uploadTime.replace(u'上传', '')
        if uploadTime.find('-') != -1:
            pass
        else:
            uploadTime = common.get_current_time()
        result_dict['uploadTime'] = uploadTime

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    print html

    result_list = parse_html(html)
    return result_list


def main():
    result_list = []
    result_list = get_data('http://chuang.le.com/u/203087306/queryvideolist?callback=jQuery191016755304000198934_1490429838177&orderType=0&currentPage=1&pageSize=48&searchTitleString=&_=1490429838178')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

