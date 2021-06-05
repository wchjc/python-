# @Auther: Ninecats
# @Time: 2021/6/5 16:56
import requests

# 查询ip地址
url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

# 定义代理
proxies = {
    'http':'175.43.34.54:9999'
}
try:
    res = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    if res.status_code == 200:
        json = res.json()
        print('当前IP地址为:', json['origin'])
except:
    print('请求失败，代理ip地址不可用')