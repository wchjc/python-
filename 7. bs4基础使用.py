# @Auther: Ninecats
# @Time: 2021/6/3 17:42
import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
res = requests.get(url, headers=headers)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    r = soup.find_all('a', class_='mnav')
    for i in r:
        print(i.text)