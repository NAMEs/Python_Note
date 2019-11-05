

import requests
import re
from bs4 import BeautifulSoup

login_url = "http://61.163.231.194:8080/Lab2.0/Login.action"
user_url = "http://61.163.231.194:8080/Lab2.0/student.action"

# pattern = '[0-9]{3}'
# num = re.compile()
# for i in range(1615925001, 1615925800):
data = {
        'userid': '1615925274',
        'password': '1615925274' + '#lab2018',
        'quan': 'Student'
}


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=7327F460E689DFD221280C2691F88823',
    'Host': '61.163.231.194:8080',
    'Referer': 'http://61.163.231.194:8080/Lab2.0/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
# 创建一个session对象
ss = requests.session()
# 使用session对象post
ss.post(login_url, data=data, headers=headers)
# html = requests.post(url, data=data, headers = headers)
# post后的session对象ss内保存有用户登录后的cookie，使用ss访问页面
html = ss.get(user_url)

print(html)
print(html.url)
print(html.status_code)
# print(html.text)
try:
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.title.string
    # print(title)
    if title != 'Error':    
        name = soup.select('.hidden-phone')[1].text
        name_list = soup.select('.hidden-phone')
        print(type(name_list))
        print(name_list)
        print(name)
    

except Exception as e:
    print("error:", e)


# print()
# with open(str(i)+".html", 'w', encoding='utf-8') as f:
    # f.write(html.text)
    # print("success")
# print(html.text)