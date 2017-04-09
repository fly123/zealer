#encoding=utf-8
import urllib
import time
import json
import common
import HTMLParser

cookie = 'ptui_loginuin=1196722167; pac_uid=1_1196722167; _qpsvr_localtk=0.1255577877623386; luin=o1196722167; lskey=00010000399fca27aa279e88ec11a07dc22311c70ddf42864c2a7557b2baba08de463592308cfb2876c12f8d; ptcz=49c5c3597f7ac640cf7695cc5844dea0af3e6b878ef1952dfc34c8074f5ad377; pt2gguin=o1196722167; uin=o1196722167; skey=@KtFL9YyGv; OM_EMAIL=zealeruser@zealer.com; fname=ZEALER; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F137911723_100100%2F0; userid=5039256; rmod=1; omvideotoken=fffadc7772; tvfe_boss_uuid=07540aafd0424ef1; pgv_info=ssid=s2972305454; pgv_pvid=5890095830; o_cookie=1196722167; TSID=e5jfr1rmsb4tphfr982tc9lhs6; 9e67236d07bdc7152e6e2b42b7f00f43=2e085d6ac0db5d59f3c1bdc0f501778628b7fbb0a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25225039256%2522%253Bi%253A1%253Bs%253A21%253A%2522zealeruser%2540zealer.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A11%253A%257Bs%253A6%253A%2522status%2522%253Bs%253A1%253A%25222%2522%253Bs%253A5%253A%2522email%2522%253Bs%253A21%253A%2522zealeruser%2540zealer.com%2522%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A54%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F137911723_100100%252F0%2522%253Bs%253A3%253A%2522uin%2522%253Bs%253A0%253A%2522%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A6%253A%2522ZEALER%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A26%253A%2522agreementAcceptingRequired%2522%253Bb%253A0%253Bs%253A29%253A%2522initialPasswordChangeRequired%2522%253Bb%253A0%253Bs%253A27%253A%2522initialAvatarChangeRequired%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25225039256%2522%253B%257D%257D; omtoken=fffadc7772; omtoken_expire=1491689812'


def get_html(url):
    # f = open('ttkb.html')
    # data = f.read()
    # f.close()

    data = common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['data']['list']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['title']
        result_dict['link'] = info_dict['url']
        result_dict['playCount'] = info_dict['daily_display_pv']
        result_dict['channel'] = '天天快报'
        result_dict['uploadTime'] = info_dict['uploadtime'][: len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []
    result_list = get_data('https://om.qq.com/VideoData/MediaVideoList?fields=2%7C3&source=0&page=1&limit=60&relogin=1')

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

