# import requests 

# # 但是很多网站会阻止代码访问

# # 模拟构造headers 请求头信息（键值对）

# headers = {
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
#     'Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
# }
# response = requests.get('https://www.douban.com/',headers=headers)

# print(response)   # headers 可以显示网站的headers信息


# # 构建参数的字典


import requests


kw = {
    'wd':'python'
}

response = requests.get('https://www.baidu.com/s?',params=kw)

# 编码格式不同会出现乱码
# 手动设置编码格式（防乱码）

response.encoding = 'utf-8'

print(response.text)  
