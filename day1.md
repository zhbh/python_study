###day1

1. 学习内容
	1. 爬虫知识
		1. urllib库中request，主要针对网页请求，有两个主要方法urlopen和urlretrieve
			1. 引用request
				`import urllib from request`
			2. 使用urlopen，主要读取网页内容
				1. 打开网站
					`url = request.urlopen('www.baidu.com')`
				2. 读取页面内容，但是只有html文件，其他js、css等等文件不会读取
					`url.read()`
				3. 还有其他读取方式，例如读取一行readline。
			3. 使用urlretrieve，主要下载页面内容
				1. 根据url下载整个网页，或网页某个图片、js、css文件等等
					`request.urlretrieve('www.baidu.com','保存下来文件名字.html')`
		2. urllib库中parse，有主要功能是对参数进行编码与解码，还有对url解析。
			1. 引用parse
				`import urllib from parse`
			2. 编码与解码
				1. 编码方法，网页请求对中文参数进行编码（unicode）。
					`parse.urlencode({'name':'中文'})`
				2. 解码方法，场景：还原中文
					`parse.parse_qs([...])`
			3. url解析，url有协议、端口、路径、请求参数等等字段
				1. urlparse 和 urlsplit 
				2. 两者不同点是urlparse多了一个字段params，params是指url中有冒号：解析出来。


	scrapy安装环境和初步了解
	2. django安装环境和初步了解