# 正则表达式

# \d 一个数字
# \w 一个数字或者字母
# . 匹配任意字符

# 长字符
# *任意个（包括0个）
# +至少一个
# ？0个或1个
# {n}n个字符
# {n,m}n-m个字符
# \s 一个空格（或者tab等空白符）、
 
#  进阶
# []表示范围
'''
1. [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
2. [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
3. [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
4. [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
'''
# A|B a或者b
# ^行开头 $行结束


# re模块
s = 'ABC\\-001'
# 使用r前缀，不用转义
s1 = r'ABC\-001'

import re
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：



print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print('ok')
else:
    print('failed')

# 切分字符串
print('a b   c'.split(' '))

# 如果使用正则
print(re.split(r'\s+','a b   c'))
print(re.split(r'[\s\,\;]+','a b ,,,  c; d'))

# 分组 用（）表示就是要提取的分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1))
print(m.groups())

t = '19:30:25'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
# 正则是贪婪匹配，也就是尽可能多字符
print(re.match(r'^(\d+)(0*)$','11234000').groups())

# 不贪婪，加上?
print(re.match(r'^(\d+?)(0*)$','11234000').groups())

# 编译
# 预先编译，提高效率
re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_tel.match('010-12345').groups())
print(re_tel.match('010-8682').groups())
print(re_tel.match('010-128682').groups())
'''
练习

请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
版本二可以验证并提取出带名字的Email地址：
<Tom Paris> tom@voyager.org
'''

rel_mail = re.compile(r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+$')
print(rel_mail.match('someone@gmail.com').groups())


