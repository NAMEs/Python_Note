from PIL import Image, ImageDraw, ImageFont
import random

# 随机生成背景色(RGB)
bgcolor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

# 背景的高度和宽带
height = 500
width = 500
size = (height, width)

# 创建画布
image = Image.new('RGB', size, bgcolor)
# image.show()

# 创建字体
font = ImageFont.truetype(font='BAUHS93.TTF', size=100)

# 创建画笔
draw = ImageDraw.Draw(image)
# 创建文本内容
text = 'ABCD'
# 将文本内容写入画笔中
draw.text((0, 0), text, font=font)
image.show()