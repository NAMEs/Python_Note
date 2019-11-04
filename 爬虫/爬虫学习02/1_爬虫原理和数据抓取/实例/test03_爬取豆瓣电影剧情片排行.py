from urllib import request, parse
import os
# import json

# interval_id=100%3A90 代表 豆瓣电影的百分比 100%--90%，详情见豆瓣电影剧情片排行榜
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

# 对豆瓣电影影评的爬取，主要是改变 以下两个参数， start表示开始影片序号， limit表示一次加载的数目
data = {
    "start": "20",
    "limit": "20",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}

data = parse.urlencode(data).encode()

req = request.Request(url, data=data, headers=headers)
response = request.urlopen(req)
html = response.read().decode()

print(response.geturl())
print(type(html))

if os.path.exists("../html/douban/"):
    pass
else:
    os.mkdir("../html/douban/")

with open("../html/douban/02.json", 'w', encoding="utf-8") as f:
    f.write(html)
    print("success")