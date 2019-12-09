### day4

- 学习内容
	BeautifulSoup作用于数据提取，针对html的DOM进行解析，查找数据。相比Xpath，是根据整个文档进行查询，效率比较低。
- 安装与引用
	- 安装 `pip2 install bs4`
	- 引用 `from bs4 import BeautifulSoup`
- 使用
	- soup = beautifulSoup('a.html','lxml') # 第二个参数是解析器，一共有4个解析器，考虑容错率和速度，容错率最好的是`html5lib`,速度比较一般是`html.parse`
	- find() 查找到第一个数据
	- find_all() 查找全部数据，返回数组列表
		```
		# 获取标签
		bs = soup.find_all('tr')
		# 获取第二个标签
		bs = soup.find_all('tr',limit=2)[1] # 使用limit参数限制获取数量；从0个开始；
		# 获取class='even'的tr标签
		bs = soup.find_all('tr',class_='even') # class与python关键字冲突，所以用 class_
		or
		bs = soup.find_all('tr',atrts={'class'='even'})
		print # 打印出来element.tag对象，可以用list(bs)打印查看到具体数值
		# 获取标签的属性值
		for element in bs:
			print element['href']
			or
			print element.attr['href']
		# 获取标签的文本值
		# 提示获取结果是数组，可以用数组列表的语法特性，有效提高写代码效率，例如arr[1:]，获取元素第一个以后全部数据。
		trs = soup.find_all('tr')[1:]
		for tr in trs:
			td =  tr.find_all()
			print td[0].string # td标签的文本值，缺点是每一个标签都是用`.string`
		```
	- strings，返回非标签的生成器，可以返回全部字符串形式，但是可能返回换行符等等
		```
		list(tr.strings) # list返回数组格式显示，也用可能数据有空白/换行符
		list(tr.strip_strings) # 返回非空白的文本
		```
	- get_text，返回子标签的的字符串，而不是生成器
	- select 可用与查找css的标签，类似jquery
	```
	select('a.even')
	```
	- 其他
		- 标签下有注释的话，string返回 None，而contents则返回全部数据列表。如果获取注释，可以用`div.comment`；
		- children，返回标签下数组的迭代器。
		- 数据类型，有Tag/NavigatableString(继承python的str)/BeautifulSoup(继承Tag)/Comment(继承NavigatableString)


