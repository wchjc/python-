# @Auther: Ninecats
# @Time: 2021/6/5 14:51
import requests,json
import re

url = 'https://old.lmonkey.com/ask'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
res = requests.get(url, headers=headers)
if res.status_code == 200:
    with open('./ylrc.html', 'w', encoding='utf-8') as fb:
        fb.write(res.text)

    # 解析数据  标题，作者，时间，url
    titles = re.findall('<div class="topic_title mb-0 lh-180 ml-n2">(.*)<small', res.text)
    dates = re.findall('<span data-toggle="tooltip" data-placement="top" title="(.*)">', res.text)
    authors = re.findall('<strong>(.*)</strong>', res.text)
    urls = re.findall('<a href="(https://old.lmonkey.com/ask/\d*)" target="_blank">', res.text)

    # print(list(zip(titles, authors, dates, urls)))
    data_json = [{'title': i[0], 'author': i[1], 'date': i[2], 'url': i[3]} for i in list(zip(titles, authors, dates, urls))]

    # 写入数据
    with open('./ylrc.json', 'w', encoding='utf-8') as fb:
        json.dump(data_json, fb)