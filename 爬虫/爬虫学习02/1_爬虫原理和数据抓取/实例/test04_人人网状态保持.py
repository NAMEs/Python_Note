from urllib import parse, request
import os

url = "http://sc.renren.com/scores/mycalendar"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": "anonymid=jo6sr79k40ag06; _r01_=1; __utma=151146938.1258973640.1541599502.1541599502.1541599502.1; __utmz=151146938.1541599502.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/968602505/profile; depovince=HEN; jebecookies=d3456bf0-7740-4a39-ad62-2a3d0ad53d41|||||; ick_login=83d066d1-b4ca-4d9e-b078-027f3a2c2d93; _de=808C2653025A488A50C4B45F09ACB784; p=c29b216417e8eebad54d3a0125bd88396; first_login_flag=1; ln_uact=13193820382; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=2df062351d615131a3d82d17c86e70386; societyguester=2df062351d615131a3d82d17c86e70386; id=968608156; xnsid=69c4a89a; ver=7.0; loginfrom=null; jebe_key=677bb307-0e02-4841-bef6-440071dd690f%7Cf32e82e144a38fbd54204d837fb67154%7C1553003684373%7C1%7C1553003538532; JSESSIONID=abcd77ItsoXPt5EY8owMw; wp_fold=0",
}

req = request.Request(url, headers=headers)

response = request.urlopen(req)

html = response.read().decode("utf-8")

if os.path.exists("../html/renren/"):
    pass
else:
    os.mkdir("../html/renren/")

with open("../html/renren/01.html", 'w', encoding="utf-8") as f:
    f.write(html)
    print("success")