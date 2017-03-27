#encoding=utf-8
import urllib
import time
import json
import common


def get_html(url):
    # f = open('meipai.html')
    # data = f.read()
    # f.close()

    data = common.http_request(url)

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data
    while True:
        uploadTime, data = common.match(data, '<meta itemprop="uploadDate" content="', 'T')
        print uploadTime
        if uploadTime == '':
            break

        title, data = common.match(data, 'class="db pa pai" alt="', '"')
        print title

        url, data = common.match(data, '<a hidefocus href="', '"')
        url = 'http://www.meipai.com' + url
        print url

        result_dict = {}
        result_dict['title'] = title
        result_dict['link'] = url
        result_dict['uploadTime'] = uploadTime

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    # print html

    info_list = parse_html(html)
    # return result_list


    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['link']
        result_dict['uploadTime'] = info_dict['uploadTime']
        result_dict['channel'] = '美拍'
        result_dict['playCount'] = get_play_count(info_dict['link'])

        print result_dict
        result_list.append(result_dict)
        time.sleep(1)

    return result_list


def get_play_count_html(url):
    # f = open('meipai_playCount.html')
    # data = f.read()
    # f.close()

    data = common.http_request(url)

    return data


def parse_play_count_html(html):
    playCount = 0
    data = html

    playCount, data = common.match(data, '<meta itemprop="interactionCount" content="', '"')

    return playCount


def get_play_count(url):
    playCount = 0
    html = get_play_count_html(url)
    playCount = parse_play_count_html(html)

    return playCount


def main():
    result_list = []
    # print get_play_count('http://www.meipai.com/media/706391086')
    result_list = get_data('http://www.meipai.com/user/1083059447?single_column=0')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

