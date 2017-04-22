#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

#login_url:http://mp.uc.cn/dashboard/index
cookie = '_UP_A4A_11_=wb6a71859c644b1a8df3622ed616d797; _UP_L_=zh; _UP_F7E_8D_=0DVs3Qgdunbt5Do%2BeSx%2Ba5WwAsSGsVzdGUOU%2BWEa1%2FCQ9pt%2Flxcgspx%2F7jdZxm88%2BDZR%2F3OCavVVlSrlA%2FHE35guhUiWeFXSFrpiz7iQup7LB%2BL83Dn0lIDh36hnRcflW%2FQJYV4NNTsRzvT0bBCoNq4smQ5n13YhLbPeoOdhK0F%2B4CVxwd%2BA5kyclW53hcuTOm0qJXeruCtloTFYuruw4zWyV2TlgB%2FFkGCOYIexFJmTeYUVb7wU54InCxl1g1C0s1YxLzJs52lWdoIk19nvWfytP81cJKxfv1GfwBTrR0bS%2FBGt91fGhZMwyZvOKbU%2F8ZkbgrGvmwxqzivluzXqQHrmHUwax9fVlczEGdRq2nKEAXdGCfg4Fw%3D%3D; _UP_D_=pc'

def get_html(url):
    # f = open('uc.html')
    # data = f.read()
    # f.close()

    data = my_common.http_request(url, cookie)

    return data


def parse_html(html):
    result_list = []
    data = html
    print data
    info_list = json.loads(data)['data']
    print info_list

    for info_dict in info_list:
        result_dict = {}
        result_dict['title'] = info_dict['article_title']
        result_dict['link'] = 'http://v.mp.uc.cn/video.html?uc_param_str=frdnsnpfvecpntnwprdsssnikt&client=ucweb&wm_aid=%s&wm_id=e7efed72e3a44db88d4d39d79adeca82&pagetype=share&btifl=10016' % info_dict['article_id']
        result_dict['playCount'] = info_dict['total_video_play_times']
        result_dict['channel'] = 'UC'
        result_dict['uploadTime'] = info_dict['publish_at'][ : len('2017-03-25')]

        result_list.append(result_dict)

    return result_list


def get_data(url):
    result_list = []

    html = get_html(url)
    result_list = parse_html(html)

    return result_list


def main():
    result_list = []

    before_day = my_common.get_before_time(30)[: len('2017-03-23')].replace('-', '')
    today = my_common.get_current_time()[: len('2017-03-23')].replace('-', '')
    url = 'http://mp.uc.cn/v2/api/ws/stat/article?size=10&begin_date=%s&end_date=%s&page=1&merge_by_date=0&create_limit=1&article_ctg=1&export_excel=0&_=1490591318060' % (before_day, today)
    result_list = get_data(url)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

