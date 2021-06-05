# @Auther: Ninecats
# @Time: 2021/6/5 16:04
import requests


def fy(kw):
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {
        'i': kw,
        'doctype': 'json'
    }

    res = requests.post(url, data=data)
    if res.status_code == 200:
        res_json = res.json()
        print('翻译内容：', res_json['translateResult'][0][0]['tgt'])
    else:
        print('翻译失败...')


tip = '''
=====================
== 欢迎使用PY翻译工具 ==
== 输入你想翻译的内容 ==
==  输入Q，退出软件  ==
=====================
'''
print(tip)

while True:
    kw = input('输入要翻译的内容：')
    if kw == 'q':
        break
    fy(kw)