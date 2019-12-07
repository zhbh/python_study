###day3

- Xpath
	- [语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)
	- 安装 
		`pip2 install Xpath`
	- 注意事项
		1. / 和 //，/ 是开头写，/ 是获取根节点；不是开头，获取子节点。 // 获取全部节点（包括子节点）
			```
			/html/body/div[@id="id_1"]
			//div[@class="perfect"]
			```
		2. contains获取某个属性的节点
			```
			//div[contains(@class,'job_detail')]
			```
		3. 谓语中下标从1开始，不是0开始
- Lmxl，用这个库解析html
	- 引用
		`from lxml import etree`
	- html字符串，字符串块用""" """
		```
		str = """
				<html>
					<div>
						<a href=""></a>
					</div>
				</html>
			  """
		htmlElement = etree.HTML(str)
		```

	- html文件，默认用xml解析html
		```
		htmlElement = etree.parse("jd.html")
		print(etree.toString(htmlElement,encoding='utf-8').decode('utf-8'))
		```
	- html文件，可能里面存在缺失一些标签，导致错误，所以指定用html解析
		```
		parse = etree.HTMLParse(encoding="utf-8")
		htmlElement = etree.parse("jd.html",parse=parse)
		print(etree.toString(htmlElement,encoding='utf-8').decode('utf-8',errors="ignore"))
		```
	- xpath语法
		- 获取html标签，etree解析html之后，用element调用xpath()方法
			`div = element.xpath('//a[class="happy"]')`
		- 获取标签的属性里的内容
			`arr = element.xpath('//a/@href')`
		or 
			`arr = element.xpath('@href')`
		- 获取标签的文本
			`arr = element.xpath('//tr/text()')`
		- 获取某个标签之后，再获取子标签，如用用“//”会重新从整个页面获取
			```
			arr1 = element.xpath('//tr')
			arr2 = element.xpath('./a')
			```
- 实战
	- 链接拼接
		`map(lambda url:BASE_URL+url,detail_url)`
	- 页码变化
		```
		base_url = 'http://search.baidu.com/page_{}_10'
		for i in range(1,8): # 不包括8
			url = base_url.format(i)
		```
	- 编码错误
		html文件可能存在乱码，导致代码错误。
		- 在decode方法中，加上`errors = 'ignore'`，忽视错误
		- response.text不进行decode，需要的时候再decode()
	- 字符串的操作
		startwith()
		replace()
		strip()去掉前后空
	- for操作
		```
		for index,object in enumerate(data):
		```