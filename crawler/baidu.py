#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

cookie = 'BDUSS=3BiREdobjM5SWJsam5-bHNXVFhianNsazktWi1DR0tlYjkxWjdodzlhZVhQeWhaSVFBQUFBJCQAAAAAAAAAAAEAAAADmRtNzdu5~rn-0b3RvdG9NjIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJeyAFmXsgBZN; BAIDUID=0E3028564DE3868F6ABE19D7AE76E9D4:FG=1'


def get_cookie(url, data = ''):
    response = my_common.get_response(url, data)
    print dir(response.headers)
    #print response.items()
    for k, v in response.headers.items():
        print k, '  ', v
    #print response.headers.getheaders('Set-Cookie')
    print response.headers.getheaders('Set-Cookie')
    res_cookie = response.headers.getheaders('Set-Cookie')
    # print response.getcode()
    # response_url = response.geturl()
    result = res_cookie[0].split(';')[0]

    return result


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
    # global cookie
    # post_data = 'staticpage=http%3A%2F%2Fv.baidu.com%2Fbrowse_static%2Fcommon%2Fhtml%2Fv3Jump.html&charset=UTF-8&token=8f6db51af16e16bb3685186595d620ef&tpl=vd&subpro=&apiver=v3&tt=1493216537818&codestring=&safeflg=0&u=http%3A%2F%2Fv.baidu.com%2Fpgc%2Flogin&isPhone=false&detect=1&gid=A7061B1-768A-4212-B292-5029259F7D48&quick_user=0&logintype=dialogLogin&logLoginType=pc_loginDialog&idc=&loginmerge=true&splogin=rate&username=13389622309&password=GY9yLFQCq%2B6NNJ41at51PPep0IpV3BzqJpha8N0ZqP%2BFLg8dLsXTAsdoMNK2b30Ee1%2FOR%2F0B0VnSF3YaQ1%2BZjy%2BswubvnyFl0Az5XSj%2FGk8dbvj4fF50Rl0q5HkSbTu%2FwxRIYLdzIbcpX8iAtN94y26Au6Vl2%2FHFAjH8tYo%2FWNc%3D&mem_pass=on&rsakey=KdpJzFMudPy4teWH2O9KyR6K10uTTITR&crypttype=12&ppui_logintime=14425&countrycode=&dv=MDEwAAoAkAAKAbEAFAAAAF00AAgCAB_d34uLa2trRjhsLWMkdjd6JXoqeSl2ThFOPUgqRy5aDQIAHcvL3_nhtfS6_a_uo_yj86Dwr5fIl-eG9YbxnuyIDQIAHcvL38XdiciGwZPSn8Cfz5zMk6v0q9u6ybrNotC0DQIAHcvLxDggdDV7PG4vYj1iMmExblYJViZHNEcwXy1JBwIABMvLy8sGAgAoy8vLy8vLy8vLy84hISEg9vb28PDw8POTk5OVlZWVlvb29vDw8PDzyxACAAHLFwIACsrIkpKXsID4wPEEAgAGycnLyv_IFQIACMvLypE7mG7MBQIABMvLy8EBAgAGy8PDzMU6FgIAIuqe9cXr3-3c693l3OnR5dDl0-vb7t_r0uHT4tTh0-DZ6N8TAgAgy9fX17_Lv8_12vWDrc-ux6PW-Jv0mbbGocLtge6J4I4IAgAJy8-LigcHBxX4CQIADMvP2dkxMTExMSU6OgcCAATLy8vLCQIAIt3fq6tLS0tLS310dCBhL2g6ezZpNmY1ZToCXQJxBGYLYhYHAgAEy8vLyw0CABvLy_3s-q7voea09bjnuOi767SM04z_iuiF7Jg&callback=parent.bd__pcbs__t7pmzc'
    # cookie = get_cookie('https://passport.baidu.com/v2/api/?login', post_data)
    # print cookie

    result_list = []
    result_list = get_data('http://v.baidu.com/wemedia/getvideo?callback=jQuery1111020405305654079675_1491730218551&start=0&num=30&_=1491730218552')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

