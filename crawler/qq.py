#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


def get_html(url):
    # f = open('qq.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url)

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data
    data = data[len('jQuery1910023629149912306913_1491655141225(') : -1]
    # print data
    info_list = json.loads(data)['videolst']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['url']

        playCount = info_dict['play_count']
        if playCount.find(u'万') != -1:
            tmp = playCount.replace(u'万', '')
            playCount = str(int(float(tmp) * 10000))
        # print playCount
        result_dict['playCount'] = playCount

        result_dict['channel'] = '腾讯视频'

        uploadTime = info_dict['uploadtime']
        if len(uploadTime) != len('2017-04-07'):
            uploadTime = my_common.get_current_time()
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

    for i in range(1, 4):
        url = 'http://c.v.qq.com/vchannelinfo?otype=json&uin=38bc45fd4c1b7fe4bafef9e42a504593&qm=1&pagenum=%s&num=30&sorttype=0&orderflag=0&callback=jQuery1910023629149912306913_1491655141225&low_login=1&_=1491655141239' % str(i)
        result_list += get_data(url)
        time.sleep(1)

    # result_list = get_data('http://c.v.qq.com/vchannelinfo?otype=json&uin=38bc45fd4c1b7fe4bafef9e42a504593&qm=1&pagenum=1&num=30&sorttype=0&orderflag=0&callback=jQuery1910023629149912306913_1491655141225&low_login=1&_=1491655141239')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

