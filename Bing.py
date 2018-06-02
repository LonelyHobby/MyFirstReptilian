import requests
kw={'q':'Python dict'}
r=requests.get('http://cn.bing.com/search',params=kw)
r.url
print(r.text)
