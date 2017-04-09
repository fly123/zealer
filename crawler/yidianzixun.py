#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser


def get_html(url):
    # f = open('yidianzixun.html')
    # data = f.read()
    # f.close()

    cookie = 'JSESSIONID=fc2b9d9cffb19f530ec60d043af298bd7a9d0f94bea38e9cb4b30547f5e35b4f; BUILD_VERSION=1490584270446; _pk_id.1.1791=3e75741ae2595c5f.1490593042.1.1490593051.1490593042.; Hm_lvt_15fafbae2b9b11d280c79eff3b840e45=1490592909,1490593140; Hm_lpvt_15fafbae2b9b11d280c79eff3b840e45=1490595241; cn_9a154edda337ag57c050_dplus=%7B%22distinct_id%22%3A%20%22158e94925b14d8-0783b59f99cf3b-5c4f231c-144000-158e94925b256f%22%2C%22%E6%9D%A5%E6%BA%90%E6%B8%A0%E9%81%93%22%3A%20%22%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201490595243%2C%22initial_view_time%22%3A%20%221481378088%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DaQn1UomHveDo4_-P82w4VnPyVXNinXZfjFiaHXZI-de8DqZau3DQYrHGVA_8T-6DvPiF1i6JD3KH_i-qt7ZLagxPVasI3pdjVPXfk850ghe%26wd%3D%26eqid%3Df5b2f8a000002c2600000006584c1a41%22%2C%22initial_referrer_domain%22%3A%20%22www.baidu.com%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201490595243%7D; UM_distinctid=158e94925b14d8-0783b59f99cf3b-5c4f231c-144000-158e94925b256f'
    data = my_common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['posts']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = 'http://www.yidianzixun.com/home?page=article&id=%s' % info_dict['news_id']
        result_dict['playCount'] = info_dict['data']['clickDoc']
        result_dict['channel'] = '一点资讯'
        result_dict['uploadTime'] = my_common.timestamp_to_str(info_dict['date'] / 1000)[: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []

    before_day = my_common.get_before_time(30)[: len('2017-03-23')]
    today = my_common.get_current_time()[: len('2017-03-23')]
    url = 'http://mp.yidianzixun.com/model/Statistic?page=1&date_end=%s&retdays=30&type=doc&date_start=%s&_rk=3792341490593085015' % (today, before_day)
    result_list = get_data(url)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

