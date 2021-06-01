import requests

url = "https://www.baidu.com"
res = requests.get(url=url)
'''
res  response对象
res.status_code  响应的状态码
res.url  请求的url
res.content   二进制内容
res.text  文本内容
res.content.decode('utf-8')  内容utf-8编码成字符串
res.headers  响应头的信息
res.request.headers  请求的请求头
res.json()  json数据
'''
print(res.request.headers)
print(res.headers)