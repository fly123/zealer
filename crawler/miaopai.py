#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser
import urllib2

cookie = 'login_state=weibo; isgroup=0; islogin=1; suid=mEpTsCBR3q2uyDUc; icon=http%3A%2F%2Ftp2.sinaimg.cn%2F3097378697%2F180%2F40060637819%2F1; loginName=paike_cblpfjcyxn; nick=ZEALER%E4%B8%AD%E5%9B%BD; url=http%3A%2F%2Fwww.yixia.com%2Fu%2Fpaike_cblpfjcyxn; token=j9QZjP8ElhSXGyUcjtOta1P62i6k8NNA; uurl=%2Fu%2Fpaike_cblpfjcyxn; h5uurl=%2Fshow%2Fu%2Fpaike_cblpfjcyxn; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215b94e58eed37a-098ed1daaf4d07-8373f6a-1327104-15b94e58eee5a5%22%7D; sensorsdata_is_new_user=true; PHPSESSID=t59aujdnrh4hrip47hjos6b5s2; SRV_CREATOR_COOKIE_LOGIN_TOKEN=j9QZjP8ElhSXGyUcjtOta1P62i6k8NNA'


def get_html(url, post_data):
    # f = open('miaopai.html')
    # data = f.read()
    # f.close()

    # data = my_common.http_request(url, cookie, post_data)
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
    request.add_header('Cookie', cookie)
    request.add_header('X-Requested-With', 'XMLHttpRequest')
    response = urllib2.urlopen(request, post_data)
    data = response.read()

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['data']['data']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['show_url']
        result_dict['playCount'] = info_dict['vcnt']
        result_dict['channel'] = '秒拍'
        result_dict['uploadTime'] = info_dict['date'].replace('.', '-')

        result_list.append(result_dict)

    return result_list


def get_data(url, post_data):
    result_list = []

    html = get_html(url, post_data)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    stTime = my_common.get_before_time(30)
    eTime = my_common.get_current_time()

    for i in xrange(1, 4):
        post_data = 'sTime=%s&eTime=%s&page=%s' % (stTime, eTime, str(i))
        result_list += get_data('http://creator.miaopai.com/statis/chan/getlist', post_data)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

