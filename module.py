
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = "Fisland"

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello,%s!' % args[0])
    else:
        print('Too many arguments')

test()
# 作用域，使用_前缀来实现
# _private 私有\

def _private_1(name):
    return "hello, %s" % name

def _private_2(name):
    return "Hi, %s" % name

def hgreeting(name):
    if len(name) > 3:
        return _private_1
    else:
        return _private_2

# if __name__ == '__main__':
#     # test()
#     hgreeting("H")


# hgreeting("H")
# hgreeting("Peter")

from PIL import Image

im = Image.open("/Users/fisland/work/Py_study/wallpaper.jpg")
print(im.format, im.size, im.mode)

im.thumbnail((200,100))
im.save("/Users/fisland/work/Py_study/thumb.png","PNG")

# 模块搜索路径
# sys.path 需要先import

# 添加搜索自己的搜索目录下的两种方法
# 修改sys.path

sys.path.append('/Users/fisland/work/Py_study/mycompany')
import mycompany
print(sys.path)

# 设置环境变量PYTHONPATH