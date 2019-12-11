### day6

- json编码与解码
	- 引用
		`import json`
	- dump & dumps
		- dump 可以使json编码成字符串进行存储，dumps 比 dump 的第二个参数可以用文件对象
		- 注意问题：
			- 文件查操作方法，无伦写和读操作，对encoding='utf-8'设置，因为默认编码格式对中文造成乱码；
			- dump操作的时候，存在中文字符，默认进行unicode进行编码，主动设置ensure_ascii=False。
	- load & loads
		- load 对json字符串进行解码，可以进行字典操作，loads 比 load 的第二个参数可以用文件对象

- csv
	- 原理
		- 纯文本
		- 每一行有记录
		- 每行有记录有分隔符
		- 每行有同样的字段序列
	- 引用
		`import csv`
	- 读取文件
		- reader
			- `res = csv.reader(fp)` # reader 是迭代器
			- `name = res[0]` # 以下标获取相关字段
		- DicReader 可以返回字典元祖数据
	- 写文件
		- writer & writerow & writerows
		```
		header = ['name','age']
		values = [
			('李丹'，20),
			('老外'，30)
		]
		with open('person.csv','w',encoding='utf-8',newline='') as fp: # newline默认的是'\n'，存储的时候，会对每行进行换行。
			writer = csv.writer(fp)
			writer.writerow(header)
			writer.writerows(values)
		```
		- DictWriter & writerheader，以字典数据写入
		```
		header = ['name','age']
		values = [
			{'name':'李丹','age':19},
			{'name':'王老','age':18}
		]
		with open('person.csv','r',encoding='utf-8',newline='') as fp:
			writer = csv.DictWriter(fp,header)
			writer.writerheader() # 写入头部，要调用writerheader方法
			writer.writerows(values) #writerow写入一条数据
		```
	