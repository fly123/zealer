#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

cookie = 'BIDUPSID=95EBC0D05830B2119AE885CE697A74F8; PSTM=1433575514; bdshare_firstime=1443623500439; BUBBLESDEl=1; BAIDUID=49F6F126A640E38A14898FB40A785747:FG=1; MCITY=-%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=7; H_PS_PSSID=22162_1439_21085_17001_22175_22160; BDUSS=RKLU5QY2RsS05zZUpPbkJzVTh5M2NDQ3RJT2xieGNKbTAxSm9va0pYQTVNeWhaSVFBQUFBJCQAAAAAAAAAAAEAAAADmRtNzdu5~rn-0b3RvdG9NjIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADmmAFk5pgBZNV'


def get_html(url):
    # f = open('baidu.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    data = data[len('/**/jQuery1111020405305654079675_1491730218551(') : -1]
    info_list = json.loads(data)['data']['videos']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['play_link']
        result_dict['playCount'] = info_dict['play_num']
        result_dict['channel'] = '百度视频'
        result_dict['uploadTime'] = my_common.timestamp_to_str(float(info_dict['update_time']))[: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://v.baidu.com/wemedia/getvideo?callback=jQuery1111020405305654079675_1491730218551&start=0&num=30&_=1491730218552')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

