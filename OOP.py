# -*- coding:utf-8 -*-
# 面向对象编程

std1 = {'name': 'Micheal', 'score': 98}
std2 = {'name': 'Peter', 'score': 88}

print(std1)
print(std2)

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def printScore(self):
        print('%s %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 70:
            return "B"
        else:
            return "C"

Micheal = Student("Micheal", 91)
Micheal.printScore()
# 类和实例

print(Micheal) #实例 带有内存地址的实例
print(Student) #类 

# 可以自由地给一个实例变量绑定属性
# ps 只是给绑定的那个有，别的实例没有，父类也不会有
Micheal.age = 11
print(Micheal.age)
print(Micheal.get_grade())
# 由于类可以起到模板的作用，因此 可以创建实例的时候，把一些必须绑定的属性强制填写进去 通过__init__方法
# 详情看以上例子

# 数据封装
# 1. 封装起来不用被看到
# 2. 可以给类增加新的方法 ps.例如 get_grade

# 访问限制
# 如果让内部属性不被外部访问，可以在属性的名称前加上两个下划线__, 将会变成一个私有变量

class Student_private(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def printScore(self):
        print('%s %s' % (self.__name, self.__score))
    
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

Mike = Student_private("Mike",99)
Mike.printScore()

# 获取可以用get方法 
# 设置可以用set方法
print(Mike.get_name())
Mike.set_score(78)

Mike.printScore()
# print(Mike._Student_private__name) 不建议

# 最后注意 自由绑定__name之后是新增一个新的属性 与class内部的__name不是同个变量

# 继承与多态
# 子类 基类，父类和超类

class Animal(object):
    def run(self):
        print('Animal is running...')


        
    

class Dog(Animal):
    def run(self):
        print('Dog is Running....')
    
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is Running....')
    
    def eat(self):
        print('Eating milk...')

dog = Dog()
dog.run()
# 存在相同的方法，子类会覆盖父类，这样就会多个好处， 多套
# isinstance() 判断某个变量是否属于某个类型

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(b, Dog))
print(isinstance(c, Animal))


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(b)

run_twice(c)

# 多态
# 调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

# 对扩展开放，允许新增Animal子类
# 对修改封闭，不需要修改依赖Animal类型的run_twice函数

# 静态语言和动态语言，Python不一定要传入Animal类型，只要保证有一样的方法
# 动态语言的鸭子类型 
# 小结，继承可以吧父类的所有功能都直接拿过来，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写


# 获取对象信息
# 对象是什么类型，有什么方法，什么属性

# type() 判断类型

print(type(123))
print(type('String'))
print(type(None))
print(type(abs))
print(type(Animal))
print(type(b))
print(type(c))

# types 定义中的常量可以判断是否函数
import types
print(type(run_twice) == types.FunctionType)
print(type(run_twice) == types.BuiltinFunctionType)
print(type(abs) == types.BuiltinFunctionType)

# 使用isinstance 可以判断继承关系

# 还可以传入tuple,是否其中之一
print(isinstance([1,2,3],(list,tuple)))


# 使用dir(),获取一个对象所有的属性和方法
# __xxx__，特殊用途，实际是调用__len__()
print(len('ABC'))
print('ABC'.__len__())

# 也可以自己定义len()
class myDog(object):
    def __len__(self):
        return 10
hhhh = myDog()
print(len(hhhh))

# 仅仅是dir列出是不够的，还需要getattr(),setattr()以及hasattr()来操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
# print(hasattr(obj, y)) throw error
setattr(obj, 'y', 'hello y')
print(hasattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 404))

# 也可以获取对象的方法
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())
# 一个正确的使用例子

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
    
'''
print(dir(123))
print(dir(c))
'''

# 实例属性和类属性

# 给实例绑定属性的方法是通过实例变量，或者通过self变量
# class中定义属性，这种属性是雷属性，归类所有

class People(object):
    name = 'Student'        
    def __init__(self, name):
        self.name = name
p = People('Peter')
# p.sore = 90
# print(p.sore)
# print(p.name)
# p = People()
print(People.name)

# 不适用相同的名字
# 向上寻找，记住这个