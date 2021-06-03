import requests
from urllib.parse import quote, urlencode
from lxml import etree


class Register():
    register_url = 'http://www.xs5200.com/register.php?do=submit'
    login_url = 'http://www.xs5200.com/login.php?jumpurl=http://www.xs5200.com/'
    bookcase_url = 'http://www.xs5200.com/modules/article/bookcase.php'
    req = None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    def __init__(self):
        self.req = requests.session()

    def register(self):
        username = input('用户名:')
        password = input('密码：')
        email = input('邮箱：')
        data = {
            'SignupForm[username]': username,
            'SignupForm[password]': password,
            'repassword': password,
            'SignupForm[email]': email,
            'sex': 1,
            'qq': '',
            'url': '',
            'action': 'newuser',
            'submit': '提 交'
        }
        data = urlencode(data)
        register_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        res = self.req.post(url=self.register_url, headers=register_headers, data=data)
        print(res.status_code)
        print(res.text)
        if res.status_code == 200:
            html = etree.HTML(res.text)
            r = html.xpath('//title/text()')
            print(r[0])
            if r[0] != '出现错误！':
                print('注册成功，账号：{0} 密码：{1}'.format(username, password))
                return True
            else:
                print('注册失败...')
                print(html.xpath('//div[@class="c1"]//li/text()'))
                return False

    def login(self):
        username = input('请输入用户名：')
        password = input('请输入密码：')
        login_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'LoginForm[username]': username,
            'LoginForm[password]': password
        }
        data = urlencode(data)
        res = self.req.post(url=self.login_url, headers=login_headers, data=data)
        if res.status_code == 200:
            html = etree.HTML(res.text)
            r = html.xpath('//title/text()')
            print(r[0])
            if r[0] != '出现错误！':
                print('登陆成功...')
                return True
            else:
                print('登陆失败')
                return False

    # 查看书架中已收藏的书本+
    def bookcast(self):
        res = self.req.get(url=self.bookcase_url, headers=self.headers)
        if res.status_code == 200:
            html = etree.HTML(res.text)
            book_name = html.xpath('//table[@class="grid"]/tr[position() > 1]/td[1]/a/text()')
            print(book_name)


obj = Register()
# result = obj.register()
# if result:
#     print('开始登陆...')
result = obj.login()
if result:
    obj.bookcast()