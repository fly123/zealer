#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


def get_html(url):
    # f = open('acfun.html')
    # data = f.read()
    # f.close()

    res =urllib.urlopen(url)
    data = res.read()

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data

    while True:
        uploadTime, data = my_common.match(data, 'data-date="', '"')
        print uploadTime
        if uploadTime == '':
            break
        uploadTime = uploadTime.replace('/', '-')
        print uploadTime

        title, data = my_common.match(data, 'data-title="', '"')
        print title

        url, data = my_common.match(data, 'data-url="', '"')
        url = 'http://www.acfun.cn' + url
        print url

        playCount, data = my_common.match(data, '<span class="nums">', '</span>')
        print playCount

        result_dict = {}
        result_dict['title'] = title
        result_dict['link'] = url
        result_dict['playCount'] = playCount
        result_dict['channel'] = 'A站'
        result_dict['uploadTime'] = uploadTime

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://www.acfun.cn/u/537970.aspx#page=1')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

