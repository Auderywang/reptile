# # 建立图片文件夹.png (视频mp4 动图gif 百度上的图片后缀是webp)

# import requests

# url = '''https://gimg2.baidu.
# com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw1%2F
# 8c7ba2cc-7b48-4375-82d4-735ceb545084%3FimageView2%2F2%2Fw%2F1
# 080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&si
# ze=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1696916441&t=209f3959efe7653cde4
# 6a873b2920741'''

# response = requests.get(url).content   # .content 也就是字节流数据（文件，音乐，图片，视频）
#                                         # # .text  返回文本数据（代码）

# request = open('picture1.png','wb')  

# request.write(response)        # 将爬取的图片写入文件夹




# 如果要请求多个照片，则可以定义一个函数：

import requests

url = input('输入想要爬取的图片网址：')


name = input('为你的图片文件命名：')

def request_get(url):

    response = requests.get(url).content 

    request = open(f'picture/{name}.png','wb')

    request.write(response)

request_get(url)





