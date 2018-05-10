import requests

r = requests.get('https://www.baidu.com/img/bd_logo1.png')
with open('c:\\test\\baidu.png', 'wb') as fp:
     fp.write(r.content)
