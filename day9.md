### day9

- 行为链
	- 概念
		- 在页面模拟鼠标，进行操作。
	- 场景
		- 多用于测试，少用在爬虫。
	- 使用方法
	```
	# 引用
	from selenium.webdriver.common.action_chains import ActionChains
	inputTag = driver.find_element_by_id('input')
	submitTag = driver.find_element_by_id('button')
	actions = ActionChains(driver)
	actions.move_to_element(inputTag)
	actions.send_keys_to_element(inputTag,'value')
	actions.move_to_element(submitTag)
	actions.click(submitTag)
	actions.perfrom()
	```
	- 其他点击方法
	```
	click_and_hold(element) # 点击但不松开鼠标
	context_click() # 右键点击
	double_click()
	``
	[更多方法](http://selenium-python.readthedocs.io/api.html)
- cookies操作
	- 获取
	`driver.get_cookies()`
	- 根据key获取value
	`driver.get_cookies(key)`
	- 删除一个
	`driver.delete_cookie(key)`
	- 删除全部
	`driver.delete_all_cookies()`
- 隐式等待&显式等待
	- 背景
		- 很多网页动态加载页面，很有可能等待不到数据，导致执行错误。
	- 隐式等待
		- 等待一定的时间，才执行
		```
		driver.implicitly_wait(10) # 单位秒
		driver.get('http://www.baidu.com')
		```
	- 显式等待
		- 等待某个元素出现，才执行相关程序
		```
		from selenium.webdriver.support.ui import WebDriverWait
		from selenium.webdriver.support import expect_conditions as EC
		try:
			element = WebDriverWait(driver,10).until(
				EC.presence_of_element_located(By.ID,'myDynamicElement')
			)
		finally:
			driver.quit()
		```
	- 其他等待条件
	```
	presence_of_all_element_located
	```
- 切换页面，可以用javascript中window.open('url')
	```
	driver.execute_script('window.open("url")')
	driver.switch_to_window(driver.window_handles[1]) # window_handles 是一组标签
	# 查看当前url
	driver.current_url
	driver.source_page
	```
- 设置代理IP
	```
	from selenium import webdriver
	options = webdriver.ChromeOptions()
	options = add_argument("--proxy-server=http://171.39.42.45:80")
	driver = webdriver.Chrome(executable_path=path,chrome_options=options)
	driver.get('url')
	```
- WebELement元素
	 `from selenium.webdriver.remote.webelement import WebELement` # 类是获取元素的所属类，点击查看相关的方法，例如save_screenhot截图
	 `type()` # 查看类型是不是WebElement
	 `driver.save_screenhot('保存图片名字.png')` # 进行截图