# 错误、调试和测试

# 一 错误处理
'''
try:
    pass
except expression as identifier:
    pass
finally:
    pass
'''
'''
try:
    print('Try...')
    r = 10 / int('a')
    print('result = ',r)
except ZeroDivisionError as e:
    print('except : ', e)
except ValueError as e:
    print('except :', e)
finally:
    print('finally...')
print('End')
'''
# 还可以在try中传入函数

import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('10')
    except Exception as e:
        logging.exception(e)

# try:
#     bar('0')
# except ZeroDivisionError as e:
#     print('Error:', e)
# else:
#     print('no result')

# 调用堆栈 

# 记录错误

# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。


main()
print('End')

'''
    ERROR:root:division by zero
Traceback (most recent call last):
  File "/Users/fisland/work/Py_study/error,debug&tes
t.py", line 37, in main
    bar('0')
  File "/Users/fisland/work/Py_study/error,debug&tes
t.py", line 33, in bar
    return foo(s) * 2
  File "/Users/fisland/work/Py_study/error,debug&tes
t.py", line 30, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
End
'''

# 抛出错误, 自定义错误类
'''
class FooError(ValueError):
    pass

def foo1(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)
    return 10 / n

foo1('0')
'''
# 另一错误处理，向上抛
# 已经有了try系列，还是用errorValue，typeError

def foo2(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid vvalue: %s' % s)
    return 10 / n

def bar2():
    try:
        foo2('10')
    except ValueError as e:
        print('value error!')
        raise

bar2()

# 调试

# 1. print 弊端，到处是print
# 2. assert 断言
def foo3(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

def main3():
    foo3('10')

main3()

# 2.1 也不好，到处是assert, 可以启动解释器的使用使用-O 关闭assert

# 3. logging,还可以输出到文件

# 配置
# import logging
# logging.basicConfig(level=logging.INFO)
# 级别， info， debug， warning， error
s = '0'
n = int(s)
# logging.info('n = %d' % n)
print(10 / n)

# 4. pdb
# 启动python的调试器pdb，单步运行，随时查看运行状态



