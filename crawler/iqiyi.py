#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


def get_html(url):
    # f = open('iqiyi.html')
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
        result_dict = {}
        tvid, data = my_common.match(data, '<li tvid="', '"')
        print tvid
        print tvid == ''
        if tvid == '':
            break

        url, data = my_common.match(data, '<a href="', '"')
        print url

        title, data = my_common.match(data, 'data-title="', '"')
        title = HTMLParser.HTMLParser().unescape(title)
        print title

        uploadTime, data = my_common.match(data, '<span class="playTimes_status tl">', '</span>')
        uploadTime = uploadTime.replace('上传', '')
        print uploadTime
        if uploadTime.find('昨天') != -1:
            uploadTime = my_common.get_before_time(1)
        elif uploadTime.find('-') != -1:
            pass
        else:
            uploadTime = my_common.get_current_time()
        print uploadTime

        result_dict['tvid'] = tvid
        result_dict['title'] = title
        result_dict['url'] = url
        result_dict['uploadTime'] = uploadTime

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    # print html

    info_list = parse_html(html)
    # return result_list

    id_list = []
    for info_dict in info_list:
        id_list.append(str(info_dict['tvid']))

    print id_list
    id_list_str = ','.join(id_list)
    print id_list_str

    play_count_url = 'http://cache.video.qiyi.com/jp/pc/%s/?src=760859ef3a0046e0932d0381e641cbb6&callback=window.Q.__callbacks__.cb8agmjm' % id_list_str
    play_count_dict = get_play_count_dict(play_count_url)
    # print play_count_dict


    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['url']
        result_dict['uploadTime'] = info_dict['uploadTime']
        result_dict['channel'] = '爱奇艺'
        result_dict['playCount'] = play_count_dict[str(info_dict['tvid'])]

        result_list.append(result_dict)

    return result_list


def get_play_count_html(url):
    # f = open('iqiyi_playCount.html')
    # data = f.read()
    # f.close()

    res =urllib.urlopen(url)
    data = res.read()

    return data


def parse_play_count_html(html):
    result_dict = {}
    data = html

    # print data
    data = data.replace('try{window.Q.__callbacks__.cb8agmjm(', '')
    data = data.replace(');}catch(e){};', '')
    play_count_list = json.loads(data)

    for play_count_dict in play_count_list:
        for k, v in play_count_dict.items():
            result_dict[str(k)] = v

    return result_dict


def get_play_count_dict(url):
    play_count_dict = {}
    html = get_play_count_html(url)
    play_count_dict = parse_play_count_html(html)

    return play_count_dict


def main():
    result_list = []
    # print get_play_count_dict('http://cache.video.qiyi.com/jp/pc/639259600,639122600,638639400,638467700,637991800,637809300,637312700,635843000,635269800,635164700,634658800,634069900,633406400,633351900,632835400,632704600,631877300,631739800,631729000,630982100,630851600,629062600,630722800,630191700,536848400,629700100,629115200,629093600,627633500,627566800,627285700,626755300,626904100,626896400,626701800,626270900,626235900,626132900,625993000,625654900,625628300,625544800/?src=760859ef3a0046e0932d0381e641cbb6&callback=window.Q.__callbacks__.cb8agmjm')
    result_list = get_data('http://www.iqiyi.com/u/1024943162/v')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

