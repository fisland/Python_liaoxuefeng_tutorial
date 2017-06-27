# coding:utf-8
'''
# 1. 切片
L = ['Michael','Sarah','Tracy','Bob','Jack']
# 取前三个元素
print [L[0],L[1],L[2]]
# Slice 切片操作
print L[0:3]
# 如果从零开始，0可以省略 [:3]
print L[1:4]
# 倒数切片
print L[-2:]
print L[-2:-1]
# ps:倒数第一个元素的索引是-1
List = list(range(100))
print List
# 前10个
print List[:10]
# 后10个
print List[-10:]
# 前11-20
print List[10:20]
# 前10个数，每两个取一个
print List[:10:2]
# 所有的数，每五个取一个
print List[::5]
# 复制一个list
print List[:]

# tuple也可以切片，结果仍是tuple
print (0,1,2,3,4)[:3] 
# 字符串也可以看成一种list
print 'hello world'[:5]

# 迭代
# forin,抽象程度比较高级，不仅是list和tuple，还可以其他科迭代对象上
d = {'a':1,'b':2,'c':3,'d':4}
for key in d:
    print "key is : %s" % key
for value in d.values():
    print "value is : %s" % value

for key,value in d.items():
    print "key is : %s & value is : %s" % (key,value)

# 字符串也可以迭代
for item in "ABCD":
    print item

# 如何判断一个对象是否可迭代对象
# 通过collections模块中Iterable类型来判断
from collections import Iterable
print isinstance("ablc",Iterable)
print isinstance([1,2,3,4],Iterable)
print isinstance(123,Iterable)

# 实现list类似Java那下标循环，内置的enumrate
for i,value in enumerate(["a","b","c"]):
    print (i,value)
    

# 列表生成式
# 即是List Comprehensions,内置可以创建list的生成器

print list(range(1,11))

# 生成[1*1,2*2,...,10*10]
# 1.循环
L10 = []
for x in range(1,11):
    L10.append(x*x)
print L10

#列表表达式，碉堡了，列表写在前面
print [y*y for y in range(1,11)]

# 还可以后面加判断，筛选结果
print [y*y for y in range(1,11) if y % 2 != 0] 
# 还可以两层循环，全排列
print [m+n for m in "ABC" for n in "XYZ"]
# 例如列出当前目录下的所有文件和目录名
import os
print [d for d in os.listdir('.')]

# for 其实可以多个变量 dict items()
d1 = {'A':'a','B':'b','C':'c'}
print [x + " = " + y for x,y in d1.items()]
# 把list里面的大写变成小写
Lupers = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in Lupers]

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
Ltest = ['Hello', 'World', 18, 'Apple', None]
Ltest1 = [x for x in Ltest if isinstance(x,str)]
print Ltest1

# 生成器
# 一边循环一边生成的就叫生成器 generator,保存的是算法
# 很多种创建generator的方法
# 1. 把列表生成器【】改成()

'''
Lg = [x * x for x in range(10)]
print(Lg)

g = (x * x for x  in range(10))
# print next(g)//基本不用

for n in g:
    print(n)

# 斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        # print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(8)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('g return value:',e.value)
        break

# f = fib(6)

# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        Ln = [1]
        for i in range(1,int(len(L))):
            Ln.append(L[i-1] + L[i])
        Ln.append(1)
        L = Ln

n = 0
for t in triangles():
    print(t)
    n  = n + 1
    if n == 10:
        break
    

# 第二种方法，包含yield

# 迭代器
# 可以直接作用于for循环的对象统称为可迭代对象 Iterable
# 可以使用isinstance()判断一个对象是不是Iterable对象

from collections import Iterable
print(">>>>>>>>>Iterable")
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance("abc",Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

# 可以被next()函数调用并不断返回下一个值的对象成为迭代器：Iterator
# 可以使用isinstance()判断一个对象是不是Iterator对象
from collections import Iterator

print(">>>>>>>>>Iterator")
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance("abc",Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(100,Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(">>>>>>>>>iter()")
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter("abc"),Iterator))






'''
    为什么list、dict、str等数据类型不是Iterator？
    这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
'''

# 小结
'''
    凡是可作用于for循环的对象都是Iterable对象
    凡是可作用于next()函数的对象都是Iterator类型，他们表示一个惰性计算的序列；
    集合类型不是Iterator是Iterable,但是可以通过iter()函数获得一个Iterator对象
    Pythonn本质就是通过Next来实现的
'''

for item in [1,2,3,4,5]:
    pass

#  ==
    
it = iter([1,2,3,4,5])
while  True:
    try:
        x = next(it)
    except StopIteration:
        break