# @Auther: Ninecats
# @Time: 2021/6/3 16:08
import requests,json
from lxml import etree

# 访问，保存html内容到文件
url = 'https://old.lmonkey.com/essence'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
if res.status_code == 200:
    with open('./xxyd.html','w',encoding='utf-8') as fb:
        fb.write(res.text)

# 提取数据
html = etree.parse('./xxyd.html', etree.HTMLParser())
authors = html.xpath('//div[contains(@class,"list-group")]//div[contains(@class,"list-group-item")]//strong/a/text()')
titles = html.xpath('//div[contains(@class,"list-group")]//div[contains(@class,"list-group-item")]//div[contains(@class,"topic_title")]/text()')
urls = html.xpath('//div[contains(@class,"list-group")]//div[contains(@class,"list-group-item")]//div[contains(@class,"flex-fill")]/a[1]/@href')

json_data = []
for i in range(len(authors)):
    data = {
        'author': authors[i],
        'title': titles[i],
        'url': urls[i]
    }
    json_data.append(data)

# 写入数据
with open('./xxyd.json', 'w', encoding='utf-8') as fb:
    json.dump(json_data, fb)