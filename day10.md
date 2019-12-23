### day10

- tesseract
	- 图形验证码识别技术
	- 安装
	`brew install tesseract`
	- 设置环境变量
	- 命令使用tesseract识别图像
	`tesseract a.png a` # 识别a.png，保存a.txt
		- 识别率并不是十全十美
		- 默认英文，可以指定语言，使用`tesseract -h`查看帮助如何设置语言
		`tesseract --list-langs` # 查看语言列表
		`tesseract -l chi_sim` # 设置简体中文

