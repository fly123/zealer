import time
import urllib2


def http_request(url, cookie = '', data = ''):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')

    if cookie != '':
        request.add_header('Cookie', cookie)

    result = ''
    if data == '':
        response = urllib2.urlopen(request, data=None, timeout=10)
        result = response.read()
    else:
        response = urllib2.urlopen(request, data, timeout=10)
        result = response.read()

    return result


def get_cookie(url, data = ''):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
    # request.add_header('Host', 'ucenter.rrmj.tv')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')

    result = ''
    if data == '':
        response = urllib2.urlopen(request)
        print dir(response)
        result = response.read()
    else:
        response = urllib2.urlopen(request, data)
        print dir(response)
        print dir(response.headers)
        print response.headers.getheaders('Location')
        print response.getcode()
        print response.geturl()
        print response.info()
        result = response.read()

    return result


def get_current_time():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def get_before_time(day):
    return time.strftime('%Y-%m-%d', time.localtime(time.time() - int(day) * 3600 * 24))


def timestamp_to_str(timestamp):
    x = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', x)


def match(html, st_str, end_str):
    match_str = ''
    st_pos = html.find(st_str)

    # print st_pos
    if st_pos != -1:
        st_pos = st_pos + len(st_str)
        end_pos = html.find(end_str, st_pos)
        if end_pos != -1:
            match_str = html[st_pos : end_pos]
            match_str = match_str.strip()
            html = html[end_pos : ]

    return match_str, html


if __name__ == '__main__':
    print get_before_time(2)
    print timestamp_to_str(1487595085411 / 1000)
    #print get_cookie('http://ucenter.rrmj.tv/page/login', 'username=13389622309&password=2876c246e1faf92246544a7b9897e3fd')
    pass
