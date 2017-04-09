#encoding=utf-8
import urllib
import time
import json
import my_common


def get_html(url):
    # f = open('youtube.html')
    # data = f.read()
    # f.close()

    res = my_common.http_request(url)
    data = res.read()

    return data


def parse_html(html):
    result_dict = {}
    data = html
    #print data

    title, data = my_common.match(data, '<meta itemprop="name" content="', '">')
    print title
    if title == '':
        return result_dict

    playCount, data = my_common.match(data, '<meta itemprop="interactionCount" content="', '">')
    print playCount

    uploadTime, data = my_common.match(data, '<meta itemprop="datePublished" content="', '">')
    uploadTime = uploadTime[ : len('2015-03-30')]
    print uploadTime

    result_dict['title'] = title
    result_dict['playCount'] = playCount
    result_dict['uploadTime'] = uploadTime
    result_dict['channel'] = 'Youtube'

    return result_dict


def get_data(url):
    html = get_html(url)
    result_dict = parse_html(html)

    return result_dict


def get_url_list_html():
    # f = open('youtube_list.html')
    # data = f.read()
    # f.close()

    res = my_common.http_request('https://www.youtube.com/channel/UC_Ks6fcoGgv4LotTZszYs-g/videos')
    data = res.read()

    return data


def parse_url_list_html(html):
    url_list = []
    data = html

    while True:
        tmp, data = my_common.match(data, '<li class="channels-content-item yt-shelf-grid-item', '>')
        if tmp == '':
            break
        url, data = my_common.match(data, '<a href="', '"')
        url = 'https://www.youtube.com' + url
        print url

        url_list.append(url)

    return url_list


def get_url_list():
    url_list = []
    html = get_url_list_html()
    url_list = parse_url_list_html(html)

    return url_list


def main():
    result_list = []
    # print get_url_list()
    # print get_data('')

    url_list = get_url_list()
    print len(url_list)
    for url in url_list:
        result_dict = get_data(url)

        if len(result_dict) > 0:
            result_dict['link'] = url
            result_list.append(result_dict)
        time.sleep(1)
        print '-' * 100

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

