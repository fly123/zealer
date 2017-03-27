#encoding=utf-8
import urllib
import time
import json
import common
import HTMLParser


def get_html(url):
    # f = open('uc.html')
    # data = f.read()
    # f.close()

    cookie = '_uab_collina=149059124737621489186008; _umdata=769E219D506600650512742A750C8D26851A493020E0A8E46A67B714CB3E347E50F00548A5F56DB2CD43AD3E795C914C128F922E7ED3362C724AB54692AD0ABE; _UP_F7E_8D_=0DVs3QgdunZXe00d0Y4AiJpo6DCK2ABbGUOU%2BWEa1%2FCQ9pt%2Flxcgspx%2F7jdZxm88%2BDZR%2F3OCavVVlSrlA%2FHE35guhUiWeFXSFrpiz7iQup7LB%2BL83Dn0lIDh36hnRcflW%2FQJYV4NNTsRzvT0bBCoNkmF7MrfuDLiLbPeoOdhK0F%2B4CVxwd%2BA5kyclW53hcuTnfviVkzT%2F3qCJwsZdYNQtLNWMS8ybOdpVnaCJNfZ71n8rT%2FNXCSsX79Rn8AU60dG0vwRrfdXxoWLOMnjcBGTTFggY93VJqD%2BpMQFMmRjkZfZKFLbPNLR%2Bg%3D%3D; _UP_A4A_11_=wb6a71859c644b1a8df3622ed616d797; _UP_D_=pc; _UP_L_=zh; USER_TMP=5iUuJtpj6jG7SvRD__fbQQ.0UB5k0ZQiEWcsB59wplLpeMf58PskAO4cBwX9tVG7aSXr254Zd_cA-u9FSOh1Dj5e26ULRbUsA0Zl1nqT283K-0r0yFNnFNJbROk4TnzVOFSlCE8QIr2ck8YsocDe8Ab00oYnEn4CrRrhu_3H29NRR9_rQtiYKYa7MeDrGuBUbaQ6F7mULcz-XqFG2censlM_hr2fV1GpI-luyP1kIdsGULnYVMVp9jl-kA06vE4xLpdidzdP7VeZWd6zTZCe-MqndeMj19rd2TQJ-YpCABBtncE8dEVvgqE2ppsSJqVv9NQkmWke5JWWBItH17SIGyewb4oY_V9A1IsQxLXBzJ2wtEY96TpyIs9hGTYUs43X6OUJxCsJCqz0DxRq46jk3cpYCMVW6tGrzmHDSZYaLcHMu3hLPWYoL9HaRjeC8XW-iQh98H3kz0I4yzOi110NwlSGnZOJqYwAeA5A2sshXU5NPdYAyvidoyhgLz2OVY5uP7GnWsIAGpRNrZNpxZbrbhRyOvetWH6oVDMk3Do4-_PGWWe7IlYUH9m2MD4zhf3rKBVdAGmNLgXIWW-tjnCK0ZS5cRdoxeOsmYPihSk6tUwpJa6jL-nGpOyUKBzv4VyZwkk69zNaA-EA-AQMVoiUv0o43EsdkbhC3P75_8JtDhIfQqtnpSbkCol1aey-0GH1vIoKWT_zzUM9viFvuhSxPCwCNQnSwR1X9wnTPYTr-QI_FpizSR-StiXboPhvEWQXPzt1yPmx4y711tQT0IewIdwZUCYF_qupEDP9_J_HeWo6RFVc7IHS_Gh0x7OTyzIY4ai38CTfGr70UMDDLUdjyHdOjRVZS1d0RWaY6EM7rxyZg5Hw8t7PNgSTiiH4CjHx0124OhVRi5GVrCfQM7T19DN8OGptdPqimuKXz8XkUzyTj7O_UJe0GhVW2Q30j0edwv575volYuYcBREMHZyIY5z6HlTjfCiC1_ncDw7w_0spWm9oqRmZFUKvlOIgcQHmgxWgxaodYiwDSnYndl8S_x68ru64wUp1hnA7ngz-zeZtR5nthbJ8RSfx3KZM1G_Bq-RtVa8m8pYWrZgRaJU8y4wzTnp_I-ZxTWMxtBYUvO5hHYfDErEFcfA_buJt1wxctN_4flIZIvvZICD_HglqXwSQHOU3SIkIAVvHO5yDvbTl6aUKrDgX7BIgNMMtEdbT88KKeOhB-Y31iuRN8CmaCgXvC2m2fa6pccuqDiDXBkkNQb8p7T2X1j9VaxvtnAUANcVir2SdHJNmcdfwBd4WvebNaLSj6KDCf0cR2Y4IaN4CbWbxYqFEEoUA1MZp_lVcInzGXCsw-srF00aYexxkuGJsLq4uv3SVFfn2avb6LFE4Q25MUXNkgeqHw5P6xOfD4Wi9Sa3YFhPL43P-xhtOtvx.1490591308153.86400000.L6VBb56Eeu6RYZHm4IbJl694XeC0vIY7h8DsJiOrkTY'
    data = common.http_request(url, cookie)

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

    before_day = common.get_before_time(30)[ : len('2017-03-23')].replace('-', '')
    today = common.get_current_time()[ : len('2017-03-23')].replace('-', '')
    url = 'http://mp.uc.cn/v2/api/ws/stat/article?size=10&begin_date=%s&end_date=%s&page=1&merge_by_date=0&create_limit=1&article_ctg=1&export_excel=0&_=1490591318060' % (before_day, today)
    result_list = get_data(url)

    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

