# coding:utf-8
import math

#1. 函数
##抽象
# 函数就是代码抽象的方式

# 函数名其实就是指向一个函数对象的引用，完全可以吧函数名赋给一个变量，相当于给函数起了一个别名
n1 = 255
n2 = 1000

print "255 hex: %s, 1000 hex:%s" %(hex(n1),hex(n2))

#2. 定义函数
# def定义，return返回
def my_abs(x):
    #参数检查抛出
    if not isinstance (x,(int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x

# print my_abs("ABC")

# 空函数 pass
def nop():
    pass

if n1 > 200:
    pass

# 多个返回，其实是返回tuple
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100,100,60,math.pi / 6)
print (x,y)

'''
    小结
    定义函数时候，需要确定函数名和函数个数
    如果有必要，先对参数的数据类型做检查 ps:if not isinstance (x,(int,float)):
    函数体内部可以用return随时返回函数结果
    函数执行完毕之后也没有return，因为是自动return None了
    函数可以返回多个值，其实就是一个tuple
'''

'''
    练习
    请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
    ax2 + bx + c = 0的两个解。
    提示：计算平方根可以调用math.sqrt()函数：
'''

def quadratic(a,b,c):
    for i in [a,b,c]:
        if not isinstance (i,(int,float)):
            raise TypeError ("bad operand type",i)
    trangle = b**2 - 4*a*c
    delta = math.sqrt(trangle)
    if delta < 0:
        return "方程没有实根"
    elif delta == 0:
        x = -b / (a*2)
        return "方程只有一个实根 %.2f" % x
    else:
        n1 = (-b + delta ) / (2*a)
        n2 = (-b - delta ) / (2*a)
        return "方程有两个实根 分别是 %.2f 和 %.2f" % (n1,n2)

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

#3. 函数参数
def power(x):
    return x*x

#参数的默认值
#默认参数降低函数的复杂度
def power(x, n=2):
    s = 1 
    while n > 0:
        n = n-1
        s = s*x
    return s

print power(2,8)
print power(8)

# 默认参数的坑
def add_end(L = None):
    if L == None:
        L = []
    L.append("End")
    return L

print add_end([1,2,3])
print add_end(["hello","World"])
print add_end()
print add_end()

'''
    Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
'''

# 多个参数 可变参数
def calc(*numbers):
    sum1 = 0
    for n  in numbers:
        sum1 = sum1 + n * n
    return sum1

print calc(1,2,3)

nums = [1,2,3,4]
print calc(*nums)

# 关键字参数
# 可变参数允许你传入0个或者任意个参数，会自动组装为一个tuple;关键字参数允许传入0个或者任意个含参数名的参数，自动组装为一个dict

def person(name,age,**kw):
    print ('name:',name,'age:',age,'other:',kw)

person('Michael',30)
person('ken',18,city='beijing')
person('peter',24,gender='M',job='coder')

dict1 = {'city':'shanghai','job':'design'}
person('sue',18,**dict1)

# 如果要限制关键字参数的名字，就可以使用命名关键字参数。
# 例如只接受city和job作为关键字参数

# 和关键字参数**kw不同，命名关键字需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
'''
def person1(name,age,*,city,job):
    print(name,age,city,job)

person1('Jack',30,city = "beijing",job = "code")
'''
# 参数组合，
# 顺序：必选参数，默认参数，可变参数，命名关键字参数和关键字参数

# ps:*args->tuple **kw->dict

#4 递归参数
# 在函数内部，可以调用其他函数，如果一个函数在内部调用自身本身，这个函数就是递归函数。

# 例子 n! = 1x2x3x4x5x6x...xn 用fact(n)来表示
# fact(n) = n! = 1 x 2 x 3 x...x(n-1) x n = (n-1)!*n = fact(n-1)*n  
# 所以fact(n) = n*fact(n-1),只有n=1的时候需要特殊处理

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print fact(1)
print fact(5)
print fact(100)

# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
# 小心栈溢出
# fact(1000)
# 改为尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact1(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)

# print fact1(1000)

# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3,'A','B','C')

'''
小结

使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''