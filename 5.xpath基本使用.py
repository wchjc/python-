from lxml import etree

text = '''
<!DOCTYPE html>
<html>
    <head>
        <title>test</title>
    </head>
    <body>
        <ul>
            <li><a href="a.html">java工程师</a></li>
            <li><a href="b.html">python工程师</a></li>
            <li><a href="c.html">大数据分析师</a></li>
        </ul>
    </body>
</html>
'''
# 方式一
# 解析html字符串
html = etree.HTML(text)
r = html.xpath('/html/body/ul/li/a/text()')
print(r)


# 方式二，读取html文件
html = etree.parse('./xpath.html', etree.HTMLParser())
r = html.xpath('/html/body/ul/li/a/text()')
h = html.xpath('/html/body/ul/li/a/@href')
d = html.xpath('//li[@class="123" and @name="1"]/a/@href')
print(*zip(h,r))
print(list(zip(h,r)))
print(d)
