#encoding=utf-8
import urllib
import time
import json


def get_current_time():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def match(html, st_str, end_str):
    match_str = ''
    st_pos = html.find(st_str) + len(st_str)

    # print st_pos
    if st_pos != -1:
        end_pos = html.find(end_str, st_pos)
        if end_pos != -1:
            match_str = html[st_pos : end_pos]
            match_str = match_str.strip()
            html = html[end_pos : ]

    return match_str, html


def get_html(url):
    f = open('qq.html')
    data = f.read()
    f.close()

    # res =urllib.urlopen("https://v.qq.com/x/cover/vmxj2j1ujjh5sp7/q03829iscd8.html")
    # data = res.read()

    return data


def parse_html(html):
    result_dict = {}
    data = html
    #print data
    title, data = match(data, '<div class="figure_title">', '</div>')
    print title
    if title == '':
        return result_dict

    playCount, data = match(data, 'class="num _video_playnum">', '</span>')
    if playCount == '':
        return result_dict
    print playCount
    if playCount.find('万') != -1:
        tmp = playCount.replace('万', '')
        playCount  = str(int(float(tmp) * 10000))
    print playCount

    uploadTime, data = match(data, 'class="tag_item">', '</span>')
    print uploadTime
    if uploadTime == '':
        return result_dict
    uploadTime = uploadTime.replace('发布', '')

    if uploadTime.find('日') != -1:
        uploadTime = uploadTime.replace('年', '-')
        uploadTime = uploadTime.replace('月', '-')
        uploadTime = uploadTime.replace('日', '')
    else:
        uploadTime = get_current_time()
    print uploadTime

    result_dict['title'] = title
    result_dict['playCount'] = playCount
    result_dict['uploadTime'] = uploadTime

    return result_dict


def get_data(url):
    result_dict = {}

    html = get_html(url)
    tmp_dict = parse_html(html)
    if len(tmp_dict) > 0:
        result_dict['title'] = tmp_dict['title']
        result_dict['link'] = url
        result_dict['uploadTime'] = tmp_dict['uploadTime']
        result_dict['channel'] = '腾讯视频'
        result_dict['playCount'] = tmp_dict['playCount']

    return result_dict


def get_url_list_html():
    f = open('qq_list.html')
    data = f.read()
    f.close()

    # res =urllib.urlopen("http://s.video.qq.com/get_playsource?id=vmxj2j1ujjh5sp7&plat=2&type=4&data_type=2&video_type=28&range=1-37&plname=qq&otype=json&num_mod_cnt=20&callback=_jsonp_17_78a4&_t=1490183329265")
    # data = res.read()

    return data


def parse_url_list_html(html):
    url_list = []
    data = html
    data = data[len('_jsonp_17_78a4(') : -1]
    data = json.loads(data)
    data_list = data['PlaylistItem']['videoPlayList']
    print data_list
    for data_dict in data_list:
        url_list.append(data_dict['playUrl'])

    return url_list



def get_url_list():
    url_list = []
    html = get_url_list_html()
    url_list = parse_url_list_html(html)

    return url_list


def main():
    result_list = []
    #print get_data('https://v.qq.com/x/cover/vmxj2j1ujjh5sp7/q03829iscd8.html')
    print get_url_list(), len(get_url_list())

    # url_list = get_url_list()
    # print len(url_list)
    # for url in url_list:
    #     result_dict = get_data(url)
    #     result_list.append(result_dict)
    #     time.sleep(1)
    #
    # print result_list, '\n', len(result_list)
    # return result_list


if __name__ == '__main__':
    main()
