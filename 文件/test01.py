# 关于读取文件的练习
# 打开文件，三个字符一组读取内容，然后显示在屏幕上
# 每读一次，休息一秒钟
import time 

# with open(r"F:/python/文件/test02.txt", 'r') as f:			
# 	Char3 = f.read(3)
# 	print(Char3)
	
# 	time.sleep(1)

# 	while Char3:
# 		Char3 = f.read(3)
# 		print(Char3)

# 		time.sleep(1)
with open(r'F:/python/文件/test02.txt', 'r') as f:
	Char3 = f.read(3)

	while Char3:
		print(Char3)

		time.sleep(1)

		Char3 = f.read(3)
