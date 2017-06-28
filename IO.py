# input output
# 异步中的完成通知，是回调还是轮询，模型复杂度比较高

# 一，Python中的文件读写-最常见的IO操作
# 读文件，open()


pdf = open('/Users/fisland/Study/PyStudy/README.md', mode='r')

pdf.read()

pdf.close()


# 引入with
# with open("/Users/fisland/Study/PyStudy/README.md", 'r') as f:
#     print(f.read())

# read 小文件一次读取
# read(size) 不知道文件大小，部分读取
# readlines 一次读取所有内容并按行返回list

with open("/Users/fisland/Study/PyStudy/README.md", 'r') as f:
    print(len(f.readlines()))

# file-like object
# read() 方法的

# 二进制文件
f_rb = open("/Users/fisland/Study/PyStudy/ball.jpg", 'rb')
print(f_rb) #.read())

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# 编码不规范， error = 'ignore'

# 写文件
# 调用open, 传入w, wb
f = open("/Users/fisland/Study/PyStudy/README.md", 'w')
f.write('Hello world!')
f.close()

# 还是with 宝箱
with open("/Users/fisland/Study/PyStudy/README.md", 'w') as f:
    f.write('Hello world with python')

# 小结

# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。


# StringIO 和 ByteslIO
from io import StringIO
string = StringIO()
string.write('hello')
string.write(' ')
string.write('world!')
print(string.getvalue())

string = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = string.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO 操作二进制
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 操作文件和目录
import os
print(os.name)
print(os.uname())

# 环境变量，在os.version中 get,具体拿值
# print(os.environ.get('PATH'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

print(os.path.abspath('.'))

# os.path.join('/Users/fisland/Study/PyStudy','testdir')
# os.mkdir('/Users/fisland/Study/PyStudy/testdir')
# os.rmdir('/Users/fisland/Study/PyStudy/testdir')

# 使用join，不要拼接 使用split，不要拆解
# 使用splitext，获取文件的扩展名
print(os.path.splitext('/Users/fisland/Study/PyStudy/README.md')[-1])

# 重命名 rename
# 删除 remove

import shutil
# os模块的补充
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 小结
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
'''
练习
利用os模块编写一个能实现dir -l输出的程序。
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''

# 序列化 
# 变量从内存中变成可存储或传输的过程称之为序列化，叫pickling
# 反序列化
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。


# ?操作json
