from urllib.request import urlretrieve


url = 'http://zyp12581.xyz'

res = urlretrieve(url, 'hello.html')

print(res)