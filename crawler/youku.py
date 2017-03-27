#encoding=utf-8
import urllib
import time
import json
import common


def get_html(url):
    # f = open('youku.html')
    # data = f.read()
    # f.close()

    res =urllib.urlopen(url)
    data = res.read()

    return data


def parse_html(html):
    result_list = []
    data = html
    while True:
        result_dict = {}
        tmp, data = common.match(data, '<div class="v-meta-title"', '>')
        url, data = common.match(data, 'href="', '"')
        print url
        if url == '':
            break

        title, data = common.match(data, 'title="', '"')
        print title
        if title == '':
            break

        uploadTime, data = common.match(data, '<span class="v-publishtime">', '</span>')
        print uploadTime
        if uploadTime == '':
            break
        if uploadTime.find('昨天') != -1:
            uploadTime = common.get_before_time(1)
        elif uploadTime.find('前天') != -1:
            uploadTime = common.get_before_time(2)
        elif uploadTime.find('天前') != -1:
            uploadTime = common.get_before_time(uploadTime.replace('天前', ''))
        elif uploadTime.find('-') != -1 and uploadTime.find(':') != -1:
            uploadTime = common.get_current_time()[ : 4] + '-' + uploadTime.split(' ')[0]
        elif uploadTime.find('-') != -1 and len(uploadTime) == len('2016-12-30'):
            pass
        else:
            uploadTime = common.get_current_time()
        print uploadTime

        playCount, data = common.match(data, '<span class="v-num">', '</span>')
        if playCount == '':
            break
        playCount = playCount.replace(',', '')
        if playCount.find('万') != -1:
            tmp = playCount.replace('万', '')
            playCount  = str(int(float(tmp) * 10000))
        print playCount

        result_dict['title'] = title
        result_dict['playCount'] = playCount
        result_dict['uploadTime'] = uploadTime
        result_dict['link'] = url
        result_dict['channel'] = '优酷'

        result_list.append(result_dict)

    return result_list


def main():
    result_list = parse_html(get_html('http://i.youku.com/i/UMjI0ODEwMzQ4/videos?order=1&page=1&last_item=&last_pn=3&last_vid=457819530&spm=a2hzp.8253869.0.0'))
    print result_list, '\n', len(result_list)
    return result_list


if __name__ == '__main__':
    main()

