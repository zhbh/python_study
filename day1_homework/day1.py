from urllib import request,parse

req = request.urlopen('http://www.budejie.com/')
print(req.read())
request.urlretrieve('http://www.budejie.com/','baidu.html')