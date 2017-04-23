#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

cookie = 'PHPSESSID=5c4e6tudjchjh8obigt8lquur3; uuids=GJWinO5GdT1RASW%252F%252Bz9f56uPaobzyCUugu7ELV2aOW1ua1OoOP%252B8li2grTxYioRaDgyNtZVk76SHdbx80nkYTA%253D%253D; chat_token=InrxrzxqKc2hFNMj4kJh8Uwsv9n7zFWXymppx2JdFkwwzHXA6W%2BmfiI0dZ8om2R7NkQT%2Fxo2KZAMUplH1grEyAclDbaWpcum; user_id=1445619214; loginStatus=1; appId=y745wfm84i37v; navi2e3b44fd=120.92.34.102%3A80%2C1445619214; Hm_lvt_7ccf7969456c912fd7c411541b68d10d=1492944684; Hm_lpvt_7ccf7969456c912fd7c411541b68d10d=1492944900; rongSDK=websocket; 1445619214=1492876800000'


def get_html(url):
    # f = open('xiudou.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data

    while True:
        tmp, data = my_common.match(data, '<td style="text-align:none;margin:0px;padding:0px;line-height:100px;', '>')
        # print tmp
        if tmp == '':
            break

        url, data = my_common.match(data, "<a href='", "'")
        print url

        title, data = my_common.match(data, 'word-wrap:break-word;word-break:break-all;height:100px;padding:0;vertical-align: middle;text-align:center;">', '</td>')
        print title

        playCount, data = my_common.match(data, '<td style="height:100px;padding:0;vertical-align: middle;text-align:center;">', '</td>')
        print playCount

        uploadTime, data = my_common.match(data, '<td  style="height:100px;padding:0;vertical-align: middle;text-align:center;">', '</td>')
        print uploadTime
        uploadTime = uploadTime[: len('2017-03-25')]
        print uploadTime

        result_dict = {}
        result_dict['title'] = title
        result_dict['link'] = url
        result_dict['playCount'] = playCount
        result_dict['channel'] = '秀兜'
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
    # result_list = get_data('http://admin.xiudou.net/User/history_cover/status/0/p/1.html')

    for i in range(1, 6):
        url = 'http://admin.xiudou.net/User/history_cover/status/0/p/%s.html' % str(i)
        result_list += get_data(url)
        time.sleep(1)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

