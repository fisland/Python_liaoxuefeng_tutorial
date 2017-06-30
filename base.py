# coding:utf-8

# from function import my_abs
print("hello world")

# 数据类型和变量

# 字符串和编码

# print ("包含中文的str")
# print (len("ABC123"))

# print(len('中文'))

print('hi,%s,you havd $%d' % ("peter",10000))

'''
    %d 整数
    %f 浮点
    %s 字符串
    %x 16
'''

print ('%2d-%02d'%(3,1))
print ('%.2f' % 3.14159)
print ('growth rate %d%%' % 10)

s1 = 72
s2 = 85 
r = (85-72)/72.0
print ('小明去年成绩：%d,今年成绩：%d,提升了百分点：%02.2f%%' % (s1,s2,r))

#使用list 和 tuple
classmate = ["peter","sue","ane"]
print (classmate)
print (len(classmate))
print (classmate[0])
print (classmate[-1])
classmate.append("adam")
print (classmate)
classmate.insert(1,"ken")
print (classmate)
classmate.pop()
print (classmate)
classmate.pop(1)
print (classmate)
classmate[1] = "Sarch"
print (classmate)
# list 里面数据可以不同类型
L = ["ABC",1,True]
# list 可以多维数组
s = ["A","b",["d","e"],"F"]
print (s)
print (s[2][1])
L = []
print ("L:%s" % L)

#tuple 元祖
# 不可变的数组 指向不变
t = (1,2)
# print t

# ps 注意
# 如果只有一个元素的元祖，不使用“，”来消除歧义，那定义的是元祖里面的具体东西，而不是元祖
# t1 = (1)
t1 = (1,)
# print t1

Languages = [
    [["Apple"],["Google"],["MS"]],
    [["OC"],["GO"],["Python"]],
    [["1"],["2"],["3"]]
]
print(Languages[1][2])

#条件控制
age = 10
if age>18:
    print ("adult")
elif age>6:
    print ("teenager")
else:
    print ("kid")

'''
if x:
    print "True"
只要x是非零数值，非空字符串，非空list等
'''

# 再议input
birth = input('birth:')
birth = int(birth)
if birth < 2000:
    print ("00前")
else:
    print ("00后")


'''
# 循环
sum1 = 0
for i in range(101):
    sum1 = sum1 + i

print sum1

sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n -2
print sum2    
# break
# continue

#dict 和 set

d = {"Michael":97,"Peter":90,"Tracy":88}
print "Michael : %d" % d["Michael"]

d["Adam"] = 85
print d
d["Adam"] = 80
print "Tom" in d
print d.get("Tom",-1)
d.pop("Adam")
print d

# list 和 dict 对比
# list 查找、插入随着元素增加而变慢，但是dict不会
# list内存占用少，dict内存占用多
# dict用空间换时间、key是不可变对象、用的是哈希算法

# set 和dict类似，也是一组key的集合，但不存储value.由于key不能重复，没有一样的key
# 创建一个set,需要提供一个list作为输入

s = set([1,2,3,1,2,4])
s1 = set([1,9,2])
s.add(7)
s.remove(4)
# 无序 无重复元素结
print s 
print s | s1
print s & s1

# 再议不可变元素
a = ['c','b','a']
a.sort()
print a

a_str = 'abc'
a_str_1 = a_str.replace('a','D')
print a_str_1
'''
'''
总结：
list [] 可变
tuple () 不可变
dict {} key不可变
set set([]) 不可变
'''


# print ("my_abs -100 %d" % my_abs(-100))