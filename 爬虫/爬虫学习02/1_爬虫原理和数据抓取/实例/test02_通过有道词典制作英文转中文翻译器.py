"""
存在问题, 详情可以参照 ”../爬虫学习01/19.py"
"""

from urllib import request, parse
import json

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}

key = input("请输入你先查询的单词：")

data = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15529942853861",
    "sign": "df98d565e70c7ab3740ea176f0c5036b",
    "ts": "1552994285386",
    "bv": "33a62fdcf6913d2da91495dad54778d1",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
    "typoResult": "false",
}

# data 数据编码
form_data = parse.urlencode(data).encode("utf-8")

# 构建请求，需要注明 method 参数
req = request.Request(url, data=form_data, headers=headers, method="POST")

response = request.urlopen(req)

html = response.read().decode()

# json 数据转换为 字典
html = json.loads(html)

for result in html["translateResult"]:
    for i in result:
        print("{0} --> {1}".format(i['src'], i['tgt']))

