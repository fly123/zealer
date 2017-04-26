#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser
import urllib2


cookie = '__guid=ed795593-d528-4b7f-b417-5dcdf2b6bd55; __gid=196757375.164997743.1490599080768.1490610374649.7; usid=9310b07c4045791fd808f73448759478; lf=1'


def get_cookie(url, data = ''):
    response = my_common.get_response(url, data)
    print response.headers.getheaders('Set-Cookie')
    res_cookie = response.headers.getheaders('Set-Cookie')
    # print response.getcode()
    # response_url = response.geturl()
    result = res_cookie[0].split(';')[0]

    return result


def get_html(url, post_data):
    # f = open('btime.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie, post_data)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['data']['result']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['href_btime']
        result_dict['playCount'] = info_dict['readNum']
        result_dict['channel'] = '北京时间'
        result_dict['uploadTime'] = info_dict['mtime'][: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url, post_data):
    result_list = []

    html = get_html(url, post_data)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    global cookie
    post_data = 'user_name=13011873006&passwd=ndN9l2iUUK%2FnRQeeOqpC%2FcSCEwza%2Fbg9KeB7DhX4c%2FaBPXD42lQT6GbgKkLLWXbKtbp7gjDWHHWtMuPERBLGgzz4pkQxmMxUVeF5eIQ5l6ABW71ax1ARfKuqun0%2FP5W3gpQVmOg114fz1SA27BN4V5fuwjrExbiM7miFClNVNxQ%3D&remember=on&timestamp=1493215810597&jump=http%3A%2F%2Fmp.btime.com%2Findex.php%3Fro%3Dlogin%26ra%3Dindex'
    cookie = get_cookie('http://user.btime.com/loging?callback=jQuery110204716364102386039_1493215810459', post_data)
    print cookie
    time.sleep(1)
    post_data = 'updateTime=1491704960&type=0&page=1&limit=30&keyWord_title='
    url = 'http://mp.btime.com/index.php?ro=Manuscript&ra=getNewListData'
    result_list = get_data(url, post_data)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

