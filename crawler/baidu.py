#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

cookie = 'BAIDUID=95EBC0D05830B2119AE885CE697A74F8:FG=1; BIDUPSID=95EBC0D05830B2119AE885CE697A74F8; PSTM=1433575514; bdshare_firstime=1443623500439; __cfduid=dab736df2d72bab6971511e0edde637851460950729; MCITY=-340%3A; PSINO=6; H_PS_PSSID=1437_13289_21098_22175_22072; BDUSS=HNycWJRRU80bERZM2cxczhCMVg2bDJPZ1k5NmdJb0NUZTM2SWJUNEg5SkFpUkZaSVFBQUFBJCQAAAAAAAAAAAEAAAADmRtNzdu5~rn-0b3RvdG9NjIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED86VhA~OlYS; o_b_t_s=909.937.727.754.291729515514.4; BUBBLESDEl=1; BDV_TRACE=1491729525807:'


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

