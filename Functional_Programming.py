# 函数式编程
# 函数概念
# 函数式编程的概念
'''
    函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因为任意一个函数，只要输入是正确的，输出就是确定的，这种纯函数我们称之为没有副作用，而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，称之为有副作用
    函数式编程的一个特点就是，允许函数本身作为参数传入另一个函数，并允许返回一个函数
    python对函数式编程部分支持，由于使用变量，Python不是纯函数式编程
'''
# 廖雪峰这一章下的实例需要看看
# SCIP for python

# 高阶函数
# 变量可以指向函数
abs(10)
abs
x = abs(-10)
f = abs
f(-10)


# 函数名也是变量
# 传入函数，既然变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# 一个简单的高阶函数
def add(x, y, func):
    return f(x) + f(y)


print(add(-19, -10, f))
# 小结，编写高阶函数，就是让函数的参数能够接收别的函数

# map/reduce
# map 两个参数，一个函数，一个Iterable
mapL = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def mapF(x):
    return x**2


r = map(mapF, mapL)
print("map list return", list(r))
print("map list str return", list(map(str, mapL)))

# reduce 累计计算，接收两个参数，1.结果，2.下一个元素
# 比如一个序列求和
from functools import reduce


def reduceAdd(x, y):
    return x + y


def reduce10Add(x, y):
    return x * 10 + y


print(reduce(reduceAdd, mapL))
print(reduce(reduce10Add, mapL))


# 将字符串转换成int的函数
def char2num(s):
    return {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }[s]


print(reduce(reduce10Add, map(char2num, '9527')))


# 整理成一个str to int的函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char22num(s):
        return {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }[s]

    return (reduce(fn, map(char22num, s)))


print(str2int("98765"))


# 使用lambda
def str22int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str22int("987654"))


# 作业：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# q1
def normalize(name):
    return name[0:1].upper() + name[1:].lower()


print(list(map(normalize, ['iksL', 'pEter', 'woeld'])))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def pp(x, y):
        return x * y

    return reduce(pp, L)


print(prod([1, 2, 3, 4, 5]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：


def str2Float(s):
    def fn(x, y):
        return x * 10 + y

    def char22num(s):
        return {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }[s]

    s1, s2 = s.split(".", 1)
    return (reduce(fn, map(char22num, s1 + s2)) / pow(10, len(s2)))


print(str2Float("98.765"))


# filter
# 接收一个函数和序列，根据返回值是true还是false来决定保留还是丢弃该元素
def is_odd(n):
    # 奇数
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 36, 67, 45, 10])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ["A", "Z", None, "S", ""])))

# 使用filter求素数


# 从三开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
# 练习 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：


def is_palindrome(L):
    return str(L) == str(L)[::-1]


output = filter(is_palindrome, range(1, 1000))
print(list(output))

# sorted 排序算法
print(sorted([36, 12, -9, 1, 177]))
print(sorted([36, 12, -9, 1, 177], key=abs))
print(sorted(['bob', 'ax2', '9', 'Zxc']))
print(sorted(['bob', 'ax2', '9', 'Zxc'], key=str.lower))
print(sorted(['bob', 'ax2', '9', 'Zxc'], key=str.lower, reverse=True))
'''
练习
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''

L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


print(sorted(L1, key=by_name))
print(sorted(L1, key=by_score, reverse=True))


# 返回函数
# 函数作为返回值
# 实现一个可变参数的求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print("calc_sum", calc_sum(1, 2, 3, 45, 6))


# 但是不想立刻求和，而是在后面的代码中，根据需要在计算，那就可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            for n in args:
                ax = ax + n
            return ax

    return sum


f = lazy_sum(1, 2, 3, 45, 6, 7, 8)
print(f)
print(f())

# 在上面例子中，在函数lazy中又定义了函数sum，内部函数sum可以引用外部lazy的参数和局部变量，当lazy返回函数sum时候，相关的参数和变量都保存在返回的函数中，这种称为闭包的结构拥有极大的威力
# ps，在我们调用lazy的时候，每次调用都会返回新的函数，即使是传入相同的参数

f1 = lazy_sum(1, 2, 3, 45, 6, 7, 8)
f2 = lazy_sum(1, 2, 3, 45, 6, 7, 8)
print(f1 == f2)

# 闭包
# 返回的参数并没有立刻执行，而是直到调用f()才执行
# 闭包的持有，参考js


def count():
    fs = []
    for i in range(1, 4):

        def f():
            return i * i

        fs.append(f)
    return fs


f1 = count()[0]
print("only f1 :", f1())

# f1,f2,f3 = count()
# print("f1:",f1(),",f2:",f2(),",f3:",f3())

# 返回闭包记得一点，返回函数不要引用任何循环变量，或者后续会发生变化的变量

# 如果一定要使用变量怎么办，方法就是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已经绑定到函数参数的值是不变的


def count_noChange():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f11, f22, f33 = count_noChange()
print("f11:", f11(), ",f22:", f22(), ",f33:", f33())
# 缺点是代码过长，可以吃用lambed代替

# 匿名函数
# 当我们传入函数的时候，有时不需要显式地定义函数，直接传入匿名函数更加方便
# 在python中，对匿名函数提供了有限的支持，以map为例子

list1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list1)

# lambda x : x*x就等于
'''
    def f(x):
        return x * x
'''
# 关键字lambd代表匿名函数，:前面的x表示函数参数
# 匿名函数有一个限制，就是只能有一个表达式，不用写return,返回值就是该表达式的结果
# 匿名函数也有一个好处。没有函数名，也不会冲突
# 此外，匿名函数也是一个函数对象，也可以吧匿名函数赋值给一个变量，再利用变量来调用该函数
f_lambda = lambda x: x * x
print(f_lambda)
print(f_lambda(10))


# 同理，也可以吧匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


print(build)
print(build(5, 8))
print(build(5, 8)())

# 装饰器
# 由于函数也是一个对象，而且函数对象可以赋值给变量，所以，通过变量也能调用函数


def now():
    print("2017-06-13")


f = now
f()

# 函数对象有有个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)
# 想要增强now()函数的功能，比如在打印前后自动打印日志，又不希望修改now()函数的定义，这种动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是返回函数的高阶函数
import functools
def log(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        print('call %s():' % fun.__name__)
        return fun(*args, **kw)
    return wrapper

# 需要借助@log
@log
def now1():
    print('2017-06-14')
now1()

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，如下，要自定义log的文本

def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log1("excute")
def now2():
    print("2017-06-15")

now2()
print(now.__name__)
print(now1.__name__)
print(now2.__name__)

# 偏函数
print('12345')
# print(int('10101011',base = 2))

# def int2(x, base=2):
#     return int(x,base)
# print(int2('1110'))

int2 = functools.partial(int,base=2)
print(int2('11001100'))

# partial 实际上接受函数对象，*arg，**kw这3个函数

max2 = functools.partial(max,10,20)
print(max2(9,2,1))

# Python装饰器

# 第一步，有一个简单的函数，想通过代码得到这个函数的大概执行时间

import time
def deco(func):
    startTime = time.time()
    func()
    endTime = time.time()
    msecs = (endTime - startTime)*1000
    print("-> elapsed time: %f ms" % msecs)



# deco(myfunc)
# myfunc()

# 上面的做法有个问题就是所有方法调用都要改为deco(func

def deco1(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("-> elapsed time: %f ms" % msecs)
    return wrapper
'''
print ("myFunc is:",myfunc.__name__)
myfunc = deco1(myfunc)
print ("myFunc is:",myfunc.__name__)
myfunc()
'''
# 装饰器语法糖

@deco1
def myfunc():
    print('start myFunc')
    time.sleep(0.6)
    print('end myFunc')

print ("myFunc is:",myfunc.__name__)
myfunc();

# 被装饰的函数带参数

def deco2(func):
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print("-> elapsed time: %f ms" % msecs)
    return wrapper

@deco2
def addFunc(a,b):
    print("start addFunc")
    time.sleep(0.6)
    print("result is %d" % (a+b))
    print("end addFunc")

# addFunc(3,8)

# 如果多个函数多种参数
# 带参数的装饰器
def deco3(arg = True):
    if arg:
        def _deco(func):
            def wrapper(*args,**kwargs):
                startTime = time.time()
                func(*args,**kwargs)
                endTime = time.time()
                msecs = (endTime - startTime) * 1000
                print("-> elapsed time: %f ms" % msecs)
            return wrapper
    else:
        def _deco(func):
            return func
    return _deco

@deco3(False)
def myFunc3():
    print('start myFunc')
    time.sleep(0.6)
    print('end myFunc')

@deco3(True)
def addFunc3(a,b):
    print("start addFunc")
    time.sleep(0.6)
    print("result is %d" % (a+b))
    print("end addFunc")

print("----------> deco3")

print("myFunc is",myFunc3.__name__)
myFunc3()

print()

print("addFunc is",addFunc3.__name__)
addFunc3(12,9)