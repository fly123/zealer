import urllib


res =urllib.urlopen("https://v.qq.com/x/cover/vmxj2j1ujjh5sp7/q03829iscd8.html")
data = res.read()
print data
print data.find('mod_cover_playnum')
