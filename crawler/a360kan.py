#encoding=utf-8
import urllib
import time
import json
import common
import HTMLParser

cookie = '__guid=121874957.3574336066989773000.1490598833550.8323; tkuc=NDQzOTgyJm5pY2tuYW1lPVpFQUxFUkNoaW5hJnNpZ249MDVmNGRkMzgzMzUwOWFlMTc5OTM0ZDcwMjlmODFiMWR4aWFua2FudWN1aWQ9MTAwMzY3ODkzMjgmbG9naW5fdGltZT0xNDkwNzc4NDU3JnRodW1iPXQwMWRmM2ZlYTNmNGM%3D; tk_token=49b19c842d51ba2119dbe3cce8bad3eb; count=8; __huid=11a4zcMRzB+tBGnmyWBdrUr0Tg2TQgM6ExxO9uqW0dEF0%3D; crypt_code=ZjNr3G3HTycJ95DCl7%252BLk2bUBvMjJ7%252Fjb4LDacxdQylif1F6p8m%252F%252BLEUtJz38NY%252B'


def get_html(url):
    # f = open('360kan.html')
    # data = f.read()
    # f.close()

    data = common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data

    while True:
        tmp, data = common.match(data, '<ul class="videolist-line', '>')
        if tmp == '':
            break

        url, data = common.match(data, '<a href="', '"')
        print url


        title, data = common.match(data, '<p class="content">', '</p>')
        print title

        uploadTime, data = common.match(data, '上传日期：', '</p>')
        print uploadTime
        uploadTime = uploadTime[: len('2017-03-25')]
        print uploadTime

        playCount, data = common.match(data, '播放量：', '</p>')
        print playCount
        if playCount.find('万') != -1:
            tmp = playCount.replace('万', '')
            playCount = str(int(float(tmp) * 10000))
        print playCount

        result_dict = {}
        result_dict['title'] = title
        result_dict['link'] = url
        result_dict['playCount'] = playCount
        result_dict['channel'] = '360影视'
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
    # result_list = get_data('http://wemedia.360kan.com/myvideo?sort=publatest&wmid=doLnP3dieGL07A&pageno=1')

    for i in range(1, 6):
        url = 'http://wemedia.360kan.com/myvideo?sort=publatest&wmid=doLnP3dieGL07A&pageno=%s' % str(i)
        result_list += get_data(url)
        time.sleep(1)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

