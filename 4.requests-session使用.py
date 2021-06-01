import requests

url = "https://www.baidu.com"
# 需要主动记录cookie并携带cookie
# 以后都用req进行访问
req = requests.session()
req.get(url=url)