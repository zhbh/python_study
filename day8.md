### 获取ajax数据

- 用ajax接口获取数据
	- 缺点：
		1. 复杂提交参数；
		2. 容易识别是爬虫。
- 用selenium+chromedriver模拟浏览器获取数据
	- 缺点：
		1. 代码多；
		2. 性能低。

### selenium+chromedriver

- 下载chromedriver
	[chromedrive](https://sites.google.com/a/chromium.org/chromedriver/downloads)
	- 问题：放在不需要权限的英文目录
	- 其他浏览器驱动
		[firefox](https://github.com/mozilla/geckodriver/releases)
		[edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
		[safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
- 安装selenium
	`pip3 install selenium`
- 使用
	```
	from selenium import webdriver
	driver_path = r'd:\doc\chromedriver.exe' # r解析原生
	dirver = webdriver.Chrome(executable_path=driver_path) # 调用当前驱动
	driver.get('http://www.baidu.com') # 打开网址
	print(driver.page_source) # 获取源文件
	```
- 基本方法
	- 关闭标签 
		`driver.close()`
	- 关闭浏览器
		`driver.quit()`
	- 定位元素
		- 根据id查找元素
		```
		driver.find_element_by_id('id')
		driver.find_element(By.ID,'id')
		```
		- 根据类名查找元素
		```
		driver.find_element_by_class_name('class')
		driver.find_element(By.CLASS_NAME,'class')
		or
		driver.find_element_by_css_selector('class')
		```
		- 根据name查找元素
		```
		driver.find_element_by_name('email')
		driver.find_element(By.NAME,'email')
		```
		- 根据标签查找元素
		```
		driver.find_element_by_tag_name('a')
		driver.find_element(By.TAG_NAME,'a')
		```
		- 根据xpath查找元素
		```
		driver.find_element_by_xpath('//div')
		driver.find_element(By.XPATH,'//div')
		```
		- 其他
			- 如果用By获取元素，引用以下库
			`from selenium.webdriver.common.by import by`
			- 如果获取多个元素，可以find_elements_by加s；
			- 如果只是获取元素，不提交/点击数据，建议使用etree.HTML(page_source),etree.xpath获取数据，因为用c语言效率更高。
	- 交互网页（点击/选择/填数据）
		- 基本网页交互标签
			- input
			- select
			- button
			- checkbox
		- 清除input数据
		`input.clear()`
		- input添加数据
		`input.send_keys('python')`
		- checkbox和button点击
		`button.click()`
		- 选择select
		```
		# 引用
		from selenium.webdriver.support.ui import Select
		selector = Select(driver.find_element_by_name('email'))
		selector.select_by_index(1)
		selector.select_by_value('code')
		selector.select_visible_text('网址')
		#取消选中
		selector.deselect_all()
		```
