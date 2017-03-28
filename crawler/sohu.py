#encoding=utf-8
import urllib
import time
import json
import common


def get_html(url):
    # f = open('sohu.html')
    # data = f.read()
    # f.close()

    res =urllib.urlopen(url)
    data = res.read()

    return data


def parse_html(html):
    result_list = []
    data = html
    print data

    data = data.strip()
    data = data[len('jQuery1720737871223479664_1490263943803( ') : -len(' );')]
    print data

    info_list = json.loads(data)['data']['list']
    print info_list
    result_list = info_list

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    # print html

    info_list = parse_html(html)
    # return result_list

    id_list = []
    for info_dict in info_list:
        id_list.append(str(info_dict['id']))

    print id_list
    id_list_str = '|'.join(id_list)
    print id_list_str

    play_count_url = 'http://vstat.v.blog.sohu.com/dostat.do?method=getVideoPlayCount&v=%s&n=bvid' % id_list_str
    play_count_dict = get_play_count_dict(play_count_url)

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['url']
        result_dict['uploadTime'] = common.timestamp_to_str(info_dict['uploadTime'] / 1000)[ : len('2017-01-05')]
        result_dict['channel'] = '搜狐视频'
        result_dict['playCount'] = play_count_dict[str(info_dict['id'])]

        result_list.append(result_dict)

    return result_list


def get_play_count_html(url):
    # f = open('sohu_playCount.html')
    # data = f.read()
    # f.close()

    res =urllib.urlopen(url)
    data = res.read()

    return data


def parse_play_count_html(html):
    result_dict = {}
    data = html

    data = data[len('var bvid=') : -1]
    play_count_list = json.loads(data)

    for play_count_dict in play_count_list:
        result_dict[play_count_dict['id']] = play_count_dict['count']

    return result_dict


def get_play_count_dict(url):
    play_count_dict = {}
    html = get_play_count_html(url)
    play_count_dict = parse_play_count_html(html)

    return play_count_dict


def main():
    result_list = []
    result_list = get_data('http://my.tv.sohu.com/user/wm/ta/v.do?callback=jQuery1720737871223479664_1490263943803&uid=175880212&pg=2&size=50&sortType=2&_=1490263943890')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

