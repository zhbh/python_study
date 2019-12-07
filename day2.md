### day2

1. 代理地址
	- 原理：代理地址相当于中间商，先请求代理地址，代理地址再次请求目标地址，就是间接请求目标地址。
	- 场景：有的网站禁止请求频繁的ip地址
	- 查看当前自己的地址，可以使用 `http://httpbin.org`
	- 代码实现：
		1. 引用request
		`from urllib import request`
		2. 确定目标源
		`url = 'http://www.baidu.com'`
		3. 确定代理地址，有免费和付费的
			- 西刺免费代理地址
			- 快代理
			- 代理云
		4. 设置代理地址，字典类型，key可以为http/https，确定端口号。
		`handler = request.ProxyHandler({'http:'190.1.1.1:2222'})`
		5. 操作handler，构建opener
		`opener = request.build_opener(handler)`
		6. opener进行开启
		`resp = opener.open(url)` //open的参数可以url字符串，或request对象
		7. 读取目标地址
		print(resp.read())
2. cookie
	- 原理：http是无序状态的，可以用cookie携带信息给服务器，内容大小4kb
	- 场景：网页登陆
	- 格式：name/value，期限expires，请求方式http/https，作用域domain（一级，二级），路径path（默认根目录）
	- 代码实现：
		- 基本
			1. 在Request的header加入Cookie，其中的值从之前页面登录之后复制。
			2. 计算机执行用bytes，而显示str；网页保存时候，进行encode，读数据decode
				`with open('renren.com','w',encoding='utf-8') as fp:
					fp.write(resp.read().decode('utf-8'))`
		- CookieJar
			1. 引用
				`from http.cookiejar from CookieJar`
			2. 创建cookiejar和handler，构建opener
				`cookiejar = CookieJar()
				handler =  request.HTTPCookieProcessor(cookiejar)
				opener = request.build_opener(handler)`
			3. 第一个url为登录页面，请求登录。
				`req = requset.Resquest(login_url,headler,urlencode(data),method="POST")
				resp = opener.open(req)`
			4. 第二个url为个人主页，进行显示个人主页。
				`req = requset.Resquest(Person_url,headler)
				resp = opener.open(req)`
		- FileCookieJar把cookie以文件保存下来，MozillaCookieJar继承FileCookieJar，和LWPCookieJar也是继承FileCookieJar，但与Set-Cookie3文件兼容，主要以后可以直接从cookie文件获取cookie值进行登录。
			1. 引用
				`from http.cookiejar from MozillaCookieJar`
			2. 创建MozillaCookieJar和handler来构建opener
				`cookiejar = MozillaCookieJar()
				handler = request.HTTPCookieProcessor(cookiejar)
				opener = request.build_opener(handler)`
			3. 请求网页
				`opener.open(url)`
			4. 保存cookie
				- `cookiejar.save()`有些网页网页关闭就cookie失效，可以添加`save(ignore_discard=True)`
				- 在第二步中，创建cookiejar之后，可以`cookiejar.load(ignore_discard=True)`
3. requests库，注意有s复数
	- get方法
		1. 引用
			`import requests
			resp = requset.get(full_url,encode(data),header)`
		2. request返回的属性
			- text
				浏览器根据自己猜测进行解码，有可能出现乱码（unicode）
			- content
				网络传送和保存电脑，以bytes格式存在，用.decode('utf-8')进行解码  //可以查看网页的编码属性，gdk
			- url
				返回请求目标地址
			- encoding
				返回编码格式
			- status_code
				请求状态
		3. 可以有type()的方法测试response.text的编码方式
	- post方法，和get方法的参数差不多
		- response返回时json格式，可以用response.json()方法返回字典数据格式，而response.text返回字符串格式。
	- cookie
		- `response.cookie` 返回cookie数据
		- `response.cookie_dict()` 返回cookie的字典数据
	- proxies
		- requests.get(proxies:{'http':'1.1.1.1:1000'})，尽量选择高匿名，不要选择透明（也会识别是代理地址）。
	- session，这里session并不是web的session
		```
		session = requests.session()
		session.post(url,headers)
	  	```
	- 处理不信任的ssl证书
		`request.get(...,verify=false)`,可以忽略ssl证书，否则会报错。

