import requests

print("请输入内容：")
inp = input()
url = "https://fanyi.baidu.com/sug"
data = {
   'kw': inp
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}
res = requests.post(url=url, data=data, headers=headers)
print(res.text)
if res.status_code == 200:
    data = res.json()
    if data['errno'] == 0:
        k = data['data'][0]['k']
        v = data['data'][0]['v'].split(';')[0]
        print(k, '===', v)


