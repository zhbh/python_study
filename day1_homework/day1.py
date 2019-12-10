from urllib import request,parse
import re

# req = request.urlopen('http://www.budejie.com/')
# print(req.read())
# request.urlretrieve('http://www.budejie.com/','baidu1.html')

# + : > = 1
# str = 'ab1c'
# result = re.search('\d',str)
# print(result.group())

# 匹配：第一位1开头，第二位是34587，后9位数字随机
# str = '15666666660'
# res = re.match('1[34578]\d{9}',str)
# print( '*'*100 )
# print( res.group() )

# 匹配：邮箱sss_.ss@ss.ss
# str = 'z1.111@111h_ee111.com.cn.cn'
# res = re.match('^\D[\w\.]*\@\w+\.\w+[\.\w]*$',str)
# print('*'*100)
# print(res.group())

# 匹配：url
# str = 'ftp://122.baid.com'
# res = re.match('^(http[s]?|ftp)\://[\w\.]+$',str)
# print('*'*100)
# print(res.group())

str = """
    <html>
        <body>
            <div>hi</div>
        </body>
    </html>
    """
res = re.search('<div(.|\s)*y>',str)
# print(str)
print(res.group())



