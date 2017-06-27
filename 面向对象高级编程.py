# coding:utf-8

# 将讨论多重继承，定制类，元类

# 一 使用__slots__

# 给一个实例自由绑定新的属性或者方法，别的实例无法使用
# 要想别的实例也能使用，需要绑定在class上
# python可以动态地给class加上功能

# 使用_slots__， 限制实例的属性
# 例如只允许添加以下的属性

class Student(object):
    __slots__ = ('name', 'age')

a = Student()
a.name = 'Peter'
a.age = 11
# a.sorce = 90

# __slots__只对该类起作用，对子类不起作用

class MiddleStudent(Student):
    pass
b = MiddleStudent()
b.score = 90

# 如果子类加上slots那就是子类加上父类的slots

# 二 使用@property
# 如果想限制属性的范围
# 方法一，可以使用set_score 和 get_score来设置和获取

class Student1(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0~100')
        self._score = value

c = Student1()
c.set_score(90)

# 嫌麻烦，又想类似属性那样简单地获取。那就使用装饰器吧

# 内置@property就是负责把一个方法变成属性调用的

class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0~100')
        self._score = value

d = Student2()
d.score = 100

# 还可以只定义只读属性，不setter就可以

class Student3(object):
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('Width must be an interger!')
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('Height must be an interger!')
        self._height = value  

    @property
    def resolution(self):
        return self._width * self._height

sanxing = Screen()
sanxing.height = 100
sanxing.width = 897
print(sanxing.resolution)

# 多重继承，总觉得这玩意有点像协议
# MixIn 混合
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

# 这样就不需要复杂而庞大的继承链
class Animal(object):
    pass

class RunableMixIn(object):
    def run(self):
        print('running...')

class FlyableMixIn(object):
    def fly(self):
        print('flying...')

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal, RunableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# hhh,第一个继承是生父，后边的都是继父
# 所以，父类有重复的方法，首先继承生父的！！！

# 三 定制类

# __str__ 相当于iOS里面的描述，description

class Student4(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('Student who is %s' % self.name)
    __repr__ = __str__

s = Student4(name = 'Peter')
print(Student4(name = 'Peter'))
print(s)

# __repr__ 打印实例时候的东西

# __iter__ 想被forin的实现方法
# 返回一个迭代对象
# 例如一个菲波那切数列

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a 

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# 有点相当于对象看成dict，__getitem__的参数也可能是一个作key的object
# 还有__setitem()__ __delitem__

# for n in Fib():
#     print(n)

f = Fib()

print(f[19])
print(f[0:5])
print(f[:19])
# __getitem__ 小标，有点像

# 还需要处理list的切片方法

# __getattr__ 动态返回一个属性
# 调用不存在的score属性，只有在没有找到属性的情况下，才调用__getattr__
# 默认是none, 抛出AttrbuteError
class Student5(object):
    def __init__(self):
        self.name = "Peter"
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        # raise AttributeError('has no this attr %s', % attr)
            

s = Student5()
print(s.name)   
print(s.score)
print(s.age())
# print(s.hello)

# 写一个链式调用
class Chain(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)

# call，就可以直接对实例进行调用
class Student6(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print ('My name is %s ' % self.name)

s =Student6('Tom')
s()

# callable 判断是否能被调用

# 使用枚举类
# 是类，每个常量是class的一个唯一实例
from enum import Enum
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Jan = Month.Jan

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# value 是自动赋值给成员的int类型，默认1开始

from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day = Weekday.Mon
print(day)

# @unique 还可以检查保证没有重复值

# 访问枚举类型的若干种方法
print(Weekday.Sat)
print(Weekday['Tue'])
print(Weekday['Tue'].value)
print(Weekday(4))

# 使用元类
# type()
# 动态语言和静态语言最大的不同就是函数与类的定义，不是编译时定义的，而是运行时动态创建的
# 就是使用type来创建类的

# 步骤
# 先定义函数
def fn(self, name = 'World!'):
    print('Hello , %s.' % name)

Hello = type('Hello', (object,), dict(hello = fn))#创建Hello class

# metaclass
# 除了使用type可以创建类，还可以使用metaclass来控制了类的创建行为
'''
    但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
    连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
    所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
'''

# 自定义list增加一个add方法c
class ListMetaclass(type):
    
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass =  ListMetaclass):
    pass

list1 = MyList()
list1.add(10)
print(list1)


# metaclass使用场景， ORM：对象-关系映射 ， 一行映射为一个对象，一个类对应一个表
# 找时间补全

        
