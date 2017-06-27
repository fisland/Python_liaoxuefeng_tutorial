# coding:utf-8

import json

# 序列化到json
d = dict(name='Bob', age=20, score=90)
jsonStr = json.dumps(d)
print(jsonStr)

# 反序列化到dict
d1 = json.loads(jsonStr)
print(d1['name'])

# 类 序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('PBob', 18, 80)

# 可以传一个default 一个函数，自定义转，也可以__dict__
jsonStr_class = json.dumps(s, default=lambda obj:obj.__dict__)
print(jsonStr_class)

# 反序列化到class，那就没办法了，老老实实写一个类

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s1 = json.loads(jsonStr_class, object_hook=dict2student)
print(s1.name)

'''
小结
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''