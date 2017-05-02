#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

#login_url:http://mp.uc.cn/dashboard/index
cookie = '_uab_collina=149059124737621489186008; _UP_A4A_11_=wb6a71859c644b1a8df3622ed616d797; _umdata=769E219D506600650512742A750C8D26851A493020E0A8E46A67B714CB3E347E50F00548A5F56DB2CD43AD3E795C914C2FC7A0B20A9CC3CB5DD7F76FB24D11DE; _UP_L_=zh; _UP_F7E_8D_=0DVs3Qgdunbt5Do%2BeSx%2Ba5WwAsSGsVzdGUOU%2BWEa1%2FCQ9pt%2Flxcgspx%2F7jdZxm88%2BDZR%2F3OCavVVlSrlA%2FHE35guhUiWeFXSFrpiz7iQup7LB%2BL83Dn0lIDh36hnRcflW%2FQJYV4NNTsTgW5FHuc94SbLSQm%2BeIYnLbPeoOdhK0F%2B4CVxwd%2BA5kyclW53hcuTOm0qJXeruCtloTFYuruw4zWyV2TlgB%2FFkGCOYIexFJmTeYUVb7wU54InCxl1g1C0s1YxLzJs52lWdoIk19nvWfytP81cJKxfv1GfwBTrR0bS%2FBGt91fGhZMwyZvOKbU%2F8ZkbgrGvmwxqzivluzXqQHrmHUwax9fVlczEGdRq2nKEAXdGCfg4Fw%3D%3D; _UP_D_=pc; USER_TMP=q3J0sh9gzfW84JjGT3mcCQ.y4E2in_7b8ZVpXvxVzKy-iwdptoxH96kri0o6JkoUKTcVa3o5WxlXMXfPQhvuwpJBBTDTV-nrlwKZyWTw8ElAK1iVWdU6uUEtVnKVCs57eAF6ulOilXIuZm-uhHyYJq37VmaVngDlb9ogybzollMSLxLfuibztEDUEQsizXZfIkOiCatqtX5Ji2Qwf4bzJa0wPZUqNMDbPsGIPzgCiVUcf1zoWyZh-MDCEA1wbUVNOpymOWhrLp9EgPW1WKiFzdgcjvi7ouRZbFLBiAjMPGDofFMPvxrQX2JrF-PIaDT-SO08-5fHwzADSnIl4fqmuK8PDXpg1h--wHKwTwfdb6sN_2ag2auN28glaDA4efm3Eo3TNbopDGaHU_cIXhP63GEPzrIZRUClitfehlseJ9U6RkXVsmXP4VHFm--rZ9GmiNWkkPdoahP3kO_X2-pebJ5A1QjWseuYswmPhuOiQ0r1zKofGVmRBYsrp5skjjyw3gYxrJxoj5u-88x15-B3iipQZ8U_nJmgflsixfrokWymqEA6ZPbCnG763DckKjH49fd3JjWKOKdZz2_cqinGL-1DDLADZkOBAKC4EUks6Wmza5JwG7BMgvHWNV6boJ98ZhKJf0-aB83TNyA3XU6eYCpeS2tjx5Y9sLX9jwkD4xBzsk-z9UAl5glmY9B-32EkMGkc7DVd8iwTe-3KIZ542SSY9EObGjSRcoMoj0asGF-z1u_ddfBeZhUngn_jH5iR1X9CkRw3-7dm0hUFYXelXoF-7i-zJ2dyeh2bzJ7F_Hbg00W3M9ZD5FYn848hzfRwnmBsnr2tyFoj3y3UbcYbv25ZAm_dyOqNGsdw20s6-1e5kjLU_tPbwQ_g_O5eM8Cl3TDxyQxVUg67JIbip-M0NlL5F6I_T4wAj6TXJwXCHQC7Di2K2t2XfWE7ATC8CoU5UiCmFoDWTsI1vdQYb1OLkUsvuTHquNBXWYOeW30sib7eccez2ZZlMOTL8iitpNiNIzm7whSE5op_Q9QbqTwcbMDX1rIh24bQAvpTBVfz8B5gm1hPQpLX4WiuXcI3LKzkk0W6y_bLNJWfHZPDvq6Xpyl5BHtIMPlfck3p9tZxkB5uS466_tEOAx9wB5nYj1QOUvENpCNtJYDOux5SyZPsdF5Ie4CpTW6lzBtX--iNIgnKoSJwhLA-ZwfmLAn4gIx4ReJTdf5RWQSBBgTJuWhYFXr7Fn4n_pYTjWEsxwpWpfEtkB74s0jhmt7tkxFWHWxQyIuqlp-N9l4XfR-yuD3gzExjhVYTL0Psoaeq12rDCYwopKErTC4T77orMyCnkOu8j25S9jCYS0WiUmkL10ep5bGjT-xufpQi9AXUF5YI-RxCt9t1JNIY-CtXvDw7u0w4CRSpUG4MReTQBrIP0R0cZ6r.1492953763964.86400000.BmaZfTxlqmpl9it6lQoLwPRJE2K7-djsw74JGKiHj1g'

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
    url = 'http://mp.uc.cn/v2/api/ws/stat/article?size=50&begin_date=%s&end_date=%s&page=1&merge_by_date=0&create_limit=1&article_ctg=1&export_excel=0&_=1490591318060' % (before_day, today)
    #print url
    result_list = get_data(url)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

