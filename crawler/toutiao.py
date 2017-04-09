#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


def get_html(url):
    # f = open('toutiao.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['data']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['display_url']
        result_dict['playCount'] = info_dict['detail_play_effective_count']
        result_dict['channel'] = '今日头条'
        result_dict['uploadTime'] = my_common.timestamp_to_str(info_dict['behot_time'])[: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://www.toutiao.com/c/user/article/?page_type=0&user_id=3898259625&max_behot_time=0&count=30&as=A155288DF82995E&cp=58D8A9D9C5BEBE1')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

