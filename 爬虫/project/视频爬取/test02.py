import requests
from bs4 import BeautifulSoup

headers = {
        # ":authority": "www.vjshi.com",
        # ":method": "GET",
        # ":path": "/watch/1778305.html",
        # ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "mediav=%7B%22eid%22%3A%22242427%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22H-bGq%24Q.%2F%25%3C)T'9jZ.Bm%22%2C%22ctn%22%3A%22%22%7D; acw_tc=3da864a415425927216628378efc3a596a3f568185322589b161c2430e; UM_distinctid=16729afdd6e5be-0c14a3ab56b5d5-9393265-144000-16729afdd703b9; Hm_lvt_d50ee9203a35be45d6b0a9db1948f94e=1542592651; Qs_lvt_67539=1542592650; _jzqc=1; _jzqy=1.1542592651.1542592651.1.jzqsr=baidu.-; _jzqckmp=1; mediav=%7B%22eid%22%3A%22242427%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22H-bGq%24Q.%2F%25%3C)T'9jZ.Bm%22%2C%22ctn%22%3A%22%22%7D; _qzjc=1; CNZZDATA3911235=cnzz_eid%3D143475895-1542591556-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1542596959; _jzqa=1.1792337281110027500.1542592651.1542592651.1542600224.2; _jzqx=1.1542600224.1542600224.1.jzqsr=vjshi%2Ecom|jzqct=/hshy%2Ehtml.-; Qs_pv_67539=3700480720998400000%2C2041863780548456200%2C3050721586825089500%2C4392175862143235600%2C4148103700585248000; Hm_lpvt_d50ee9203a35be45d6b0a9db1948f94e=1542600236; _qzja=1.181136785.1542592650954.1542592650956.1542600223744.1542600223744.1542600235580.0.0.0.22.2; _qzjto=22.2.0",
        "referer": "https://www.vjshi.com/hshy.html",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

url = "https://www.vjshi.com/watch/1778305.html"
html = requests.get(url, headers = headers)

print(html)
# print(html.text)

soup = BeautifulSoup(html.text, 'lxml')

meat_url = soup.findAll('meta', {"property": "og:video"}) 

# print(len(meat_url))
print(meat_url)
video_url = meat_url[0]['content']

video_name = video_url.split('/')[-1]
video = requests.get(video_url)
print(video)

with open(video_name, 'wb') as f:
    f.write(video.content)
print("success")