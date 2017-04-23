#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

cookie = 'vjuids=752b737ed.14e0be03b5b.0.50b24e3d; _ga=GA1.2.2105536592.1490257960; JSESSIONID=abc1nxd-Oxfkj-qS-goTv; sucaccount=emVhbGVydXNlckB6ZWFsZXIuY29t|ZEALER|http://sucimg.itc.cn/avatarimg/48ece473715949ad9488c9f0638a11eb_1446728160234|o9cf4067187e545f|=v2=ecN6BXZlkGVymdbhVWFsZXIuY29t|82445926b5752|http://sucimg.itc.cn/avatarimg/48ece473715949ad9488c9f0638a11eb_1446728160234; vjlast=1434718321.1491664766.12; sohutag=8HsmeSc5Njwmcyc5NSwmYjc5MywmYSc5NCwmZjc5NCwmZyc5NCwmbjc5NjwmaSc5Nywmdyc5NCwmaCc5NCwmYyc5NCwmZSc5NCwmbSc5NCwmdCc5NH0; IPLOC=CN4403; SUV=1506142342523736; ppsmu=1|1492955594|1494165194|dXNlcmlkOjIxOnplYWxlcnVzZXJAemVhbGVyLmNvbXx1aWQ6MDp8dXVpZDowOg|CMNh1LaX8B6PPOSyoMI5TLZAAAzCZeafVRp2zXluU50zZkw0zi3YUDjSRQNp725HquacEJvGrGm3hHkKF1remQ; ppinf=2|1492955594|1494165194|bG9naW5pZDowOnx1c2VyaWQ6MjE6emVhbGVydXNlckB6ZWFsZXIuY29tfHNlcnZpY2V1c2U6MzA6MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfGNydDowOnxlbXQ6MTowfGFwcGlkOjQ6MTEzOHx0cnVzdDoxOjF8cGFydG5lcmlkOjE6MHxyZWxhdGlvbjowOnx1dWlkOjE2Om85Y2Y0MDY3MTg3ZTU0NWZ8dWlkOjE2Om85Y2Y0MDY3MTg3ZTU0NWZ8dW5pcW5hbWU6MDp8; pprdig=JjP2PcU24pQ5nKg2jwJfj0Yf1e1YW9FXHWuMJMdcSFnVp17crpo6rDrBuFkz-I9GcwkY9P47gdt-icB66aEDhlertijPJdjzaL-QG5zYQr-XZKjGkFlcHsWpSun_qg-GaPy111gpqhEGyaY-sbg3JlMLkw_xQvbVXznJ-JUchOw; spinfo=c29odXx6ZWFsZXJ1c2VyQHplYWxlci5jb218MzA0NTgyNDQ1; spsession=MzA0NTgyNDQ1fDE0OTQxNjUxOTR8MTQ5NDE2NTE5NHw4MjQ0NTkyNmI1NzUy-0Ltesz/NEFT9tgs5E7AgMoXVnT8=; lastdomain=1494165194|emVhbGVydXNlckB6ZWFsZXIuY29tfA|zealer.com|1; ppmdig=1492955594000000f22b773090235b6163a6426821e2956a'

def get_html(url):
    # f = open('shxw.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    # print data
    while True:
        tmp, data = my_common.match(data, 'node-type="article-content', 'data-id')
        if tmp == '':
            break

        url, data = my_common.match(data, '<a href="', '"')
        print url

        title, data = my_common.match(data, 'node-type="article-title" alt="', '"')
        print title

        uploadTime, data = my_common.match(data, '<span class="stat-time">', '</span>')
        print uploadTime
        uploadTime = uploadTime[: len('2017-03-25')]
        print uploadTime

        playCount, data = my_common.match(data, '<span class="stat-eye-num">', '</span>')
        print playCount

        result_dict = {}
        result_dict['title'] = title
        result_dict['playCount'] = playCount
        result_dict['uploadTime'] = uploadTime
        result_dict['link'] = url
        result_dict['channel'] = '搜狐新闻'

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('http://mp.sohu.com/v2/main/news/list.action?catId=0&column=1&pageNo=1&pageSize=30&type=0&cDraft=100000')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

