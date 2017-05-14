#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


cookie = 'yu=3337306387256; UM_distinctid=15bfd9e1a922e03-03f229797-6b12157e-1fa400-15bfd9e1aa25e66; helloService_loginok=1; Hm_lvt_cb44eb450c53c91a1cc1d2511f5919b3=1494608649; Hm_lpvt_cb44eb450c53c91a1cc1d2511f5919b3=1494608700; helloService="1QV@2x7BQN0@Jpj5x1mBotA3l84CTZld4zuMKVDwCdNLekD83OxORi8DVhTyOD6bVFLuNNwdykmlwesIhWxJf6R957mYyLVFrXz7RN@bHp6Zbrbb7GnFms8zDLOgxA1x@kDy3T8BA0R3d3YGd@VjOruaXS555DeznEGU3l8Yqnj78_LsRMwF1gGo0A7JMRSN"; helloService_username=ZEALER; helloService_login=2; helloService_userface="http://p01.v1.cn/group2/M00/10/62/ChQB0FeIYyeAL5kdAAANUCuagAw079.png"; helloService_failuretime=-1'


def get_html(url):
    # f = open('v1.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data

    while True:
        vid, data = my_common.match(data, 'name="chk_list" value="', '"')
        print vid
        if vid == '':
            break

        url, data = my_common.match(data, 'href="', '"')
        print url

        title, data = my_common.match(data, 'title="', '"')
        print title

        uploadTime, data = my_common.match(data, '<p>上传于：', '<span')
        print uploadTime
        uploadTime = uploadTime.replace('/', '-')
        uploadTime = uploadTime[: len('2017-03-25')]
        print uploadTime

        result_dict = {}
        result_dict['vid'] = vid
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
        id_list.append(str(info_dict['vid']))

    print id_list
    id_list_str = ','.join(id_list)
    print id_list_str

    play_count_url = 'http://user.v1.cn/uservideo/temp.json'
    post_data = 'vids=' + id_list_str
    play_count_dict = get_play_count_dict(play_count_url, post_data)
    # print play_count_dict

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['url']
        result_dict['uploadTime'] = info_dict['uploadTime']
        result_dict['channel'] = '第一视频'
        result_dict['playCount'] = '0'
        if play_count_dict.has_key(str(info_dict['vid'])):
            result_dict['playCount'] = play_count_dict[str(info_dict['vid'])]

        result_list.append(result_dict)

    return result_list


def get_play_count_html(url, post_data):
    # f = open('v1_playCount.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie, post_data)

    return data


def parse_play_count_html(html):
    result_dict = {}
    data = html

    print '----: ' + data
    if data.find('body') == -1:
        return result_dict
    data = data[1 : -1]
    data = data.replace('\\"', '\"')
    play_count_list = json.loads(data)['body']['data']
    print play_count_list

    for play_count_dict in play_count_list:
        vid = play_count_dict['videoId']
        playCount = play_count_dict['playNum']

        result_dict[vid] = playCount

    return result_dict


def get_play_count_dict(url, post_data = ''):
    play_count_dict = {}
    html = get_play_count_html(url, post_data)
    play_count_dict = parse_play_count_html(html)

    return play_count_dict


def main():
    result_list = []
    # print get_play_count_html('http://user.v1.cn/uservideo/temp.json')
    # print get_play_count_dict('')
    # print get_html('http://user.v1.cn/uservideo/index.jhtml?pageNo=1&pageSize=6')
    # print get_play_count_dict('http://cache.video.qiyi.com/jp/pc/639259600,639122600,638639400,638467700,637991800,637809300,637312700,635843000,635269800,635164700,634658800,634069900,633406400,633351900,632835400,632704600,631877300,631739800,631729000,630982100,630851600,629062600,630722800,630191700,536848400,629700100,629115200,629093600,627633500,627566800,627285700,626755300,626904100,626896400,626701800,626270900,626235900,626132900,625993000,625654900,625628300,625544800/?src=760859ef3a0046e0932d0381e641cbb6&callback=window.Q.__callbacks__.cb8agmjm')
    # result_list = get_data('http://user.v1.cn/uservideo/index.jhtml?pageNo=1&pageSize=6&orderby=1&publishstatus=1')

    for i in range(1, 6):
        url = 'http://user.v1.cn/uservideo/index.jhtml?pageNo=%s&pageSize=6&orderby=1&publishstatus=1' % str(i)
        result_list += get_data(url)
        time.sleep(1)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

