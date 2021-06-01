import requests

# url = "https://www.lmonkey.com/"
# res = requests.get(url=url)
# print(res.status_code)
# if res.status_code == 200:
#     with open('./test.html','w',encoding='utf-8') as fb:
#         fb.write(res.text)


url = "https://www.kuaidaili.com/free"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}

res = requests.get(url=url)
print(res.status_code)