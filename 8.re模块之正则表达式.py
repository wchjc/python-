# @Auther: Ninecats
# @Time: 2021/6/5 11:33
import re

s = 'jisjshsj521jsjs2'
reg = '\d'
res = re.findall(reg, s)
print(res)

# search 和 match
reg = 'isj'
res = re.match(reg, s)
print(res)

res = re.search(reg, s)
print(res.group())
print(res.span())

# compile
reg = '\d{3}'
reg = re.compile(reg)
res = reg.search(s)
print(res)

# ()使用
reg = '\w{4}(\d{1})'
res = re.search(reg, s)
print(res.group())
print(res.groups())