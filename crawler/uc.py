#encoding=utf-8
import urllib
import time
import json
import my_common
import HTMLParser

#login_url:http://mp.uc.cn/dashboard/index
cookie = '_uab_collina=149059124737621489186008; _UP_A4A_11_=wb6a71859c644b1a8df3622ed616d797; _umdata=769E219D506600650512742A750C8D26851A493020E0A8E46A67B714CB3E347E50F00548A5F56DB2CD43AD3E795C914C630DB9E38EA0B24A8813E54BFFF5EDC3; _UP_L_=zh; _UP_F7E_8D_=0DVs3Qgdunbt5Do%2BeSx%2Ba5WwAsSGsVzdGUOU%2BWEa1%2FCQ9pt%2Flxcgspx%2F7jdZxm88%2BDZR%2F3OCavVVlSrlA%2FHE35guhUiWeFXSFrpiz7iQup7LB%2BL83Dn0lIDh36hnRcflW%2FQJYV4NNTsRzvT0bBCoNq4smQ5n13YhLbPeoOdhK0F%2B4CVxwd%2BA5kyclW53hcuTOm0qJXeruCtloTFYuruw4zWyV2TlgB%2FFkGCOYIexFJmTeYUVb7wU54InCxl1g1C0s1YxLzJs52lWdoIk19nvWfytP81cJKxfv1GfwBTrR0bS%2FBGt91fGhZMwyZvOKbU%2F8ZkbgrGvmwxqzivluzXqQHrmHUwax9fVlczEGdRq2nKEAXdGCfg4Fw%3D%3D; _UP_D_=pc; USER_TMP=Ts6LHS5HZozOa7OheqbD3w.y6LkrhZLsM2t7z4-rwZ_ok4cdgeaCXsydDTKFdoyVsIKpj8ZW6nvQSigRhUtsiqoIE3OG7M14W7CFnZktjUq66A1y3KLilgZgXjXRbS3UPCKU4XlFyWM5AIPgWGebrUJTIxa4FpiW0PKi_u92uyr9dx8VOMBBUO21hpuufbpTBxjugYdoq2SdpuFaigY5Lq-f7G2H1o70nJvTAzMCYjAxnVOlRL00LvFk88jwwhod_7VWiIfGlKGjpbkvtpqvogxKh4hYaosg3aaYs0-RfkeNHhPRRTiCzTM7LxR3KiFnZ7UQ7XgnZYEM7-aXcBc58YIIszh7WFw82SVkjpsAYioq6RBidRYi5XrZv2GqlZkUHc7LpWyaC2zTkSbXI3N2sDZ4ijdA4WPhzwMT5516pGt-IzpMkX9YyEU4Ph0_nnsDhlDmjW-pH6n1k_JfjKRb79BKfmoSH442YyJg2hAQWF_tyVBUtmaL9LsqR3mhd9pg4_YXK-2cIpnYOrqH9CegKitJUWepjA8R0aOE8btCTL8Xp4QBLyhnpqHu_Tfig_8U_r05MObcNMTH6nVEKXUNFrOxSO9hCehzvmqbI_ZVJSn3SIxzgn1a9Xdk6q-EhBievYmjKgJcfq9GsXSEH_t5ZvJeEt92xMlDB6FcJV9KySVGqPi2hXHPVWQJhhYWXCNkPzeo3-xa1EKilJ_zCFxF49fCgctT5mnx3S6cFG-RwqaJvCD6e0JUMDSTO_zPV4QK-0WCoebKzVnx6a3aM1SSewE6jzzuNBZpUZJIDn5-MxQ2zMf3rPQD6yUFyj_0jSBqIyYfcLtwy4JoFH36SdD-zVooDD945XiahXY67SlUEyf6zRR06xzA_ZM7OZ3JEDiBCQsuAR96y85GZmhZhPOhNaNDUgHi3BPTrWcPMTMj0tYmp3TTPA5rTqIKTrOB8iftJE7_llsjP-UGJSQZx4BQyXhBBCYSI07D9YdtKt2uW0W1EgKlUvWtq5JliEF6tcQV8rapGsTIZLAL8XEMPbZS1cvJjJX8Eqik9w30S3KvqkRBt7Rida-a3nVQyFVaGtF0SAfvYw9WIeyL5YsuRP7oChzyxZGWGNwkaUfYQ7SSEjoZAaW58QwBnsBk-4Om9iUwaCEE52NWlSjsmL8fXHM5j5xS0peIMJNLAYiLc2AglnV0Js5cd3A-870GUOt0p9mVm7NwZKdRscmAi4qeEeygLga0MifPz9Pldl2Lhyp-ZJ1gfnmMq9cDnegJAI0iSpsnJoZEErkuPAVd_MjVJxytcQ4Ns0hKHF2fdQm7LJjZe73Tj5sM7mdfYnLrM0RSofMi0BdA93eQs6GTVbTuhHU9YzOwPcbi-C2laSqyoC8dYyprilOa65iSF32D8l-H2qyGMfDxOEqo1jy-mYOsh5ZjuKL.1492864452147.86400000.J9b8VLWwKdTVkaQacVXhi-x1Z6CEOmG5uyKkraof9MY'

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

