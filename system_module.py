# Datetime
# coding:utf-8

from datetime import datetime

# 获取当前
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015,4,19,12,20)
print(dt)

# Datetime转换为timestamp
print(dt.timestamp())

# timestamp转换为Datetime
timestamp1 = 1429417211.0
dt1 = datetime.fromtimestamp(timestamp1)
dt1_utc = datetime.utcfromtimestamp(timestamp1)
print(dt1)
print(dt1_utc)
# 本地时间

# str转换为datetime
cday = datetime.strptime('2017/06/29 18:00:00', '%Y/%m/%d %H:%M:%S')
print(cday)
# Datetime转换为str
print(cday.strftime('%Y/%m/%d %H:%M:%S'))

# datetime加减
# 需要引入timedelta类
from datetime import timedelta
print('now->>>>>>>>', now)
time = now + timedelta(hours = 2)
print(time)
# 本地时间转换为UTC时间  
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
print(now)
dt2 = now.replace(tzinfo=tz_utc_8)
print(dt2)
# 时区转化
# 需要的时候再看吧

# 二 collections

# 1. namedtuple
# 相当于swift里面的typelias
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.y)
print(isinstance(p, tuple))
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
# deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和张
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultDict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
# 默认值是调用函数返回的，而函数在创建defaultdict对象时候传
# 除了key不存在的时候返回默认值，其他时候与dict行为一样

# 如果要保持dict顺序，可以使用orderdict
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)

od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
# 按照插入顺序排序，而不是key本身
# 可以实现个FIFO模型 。

# counter 计数器
from collections import Counter 
c = Counter()

for ch in 'Programming':
    c[ch] = c[ch] + 1

print(c)

# base64
# Base64是一种用64个字符来表示任意二进制数据的方法。

# struct
# 解决byts和其他二进制数据类型转换

# hashlib
# md5 摘要算法

# itertools
# 操作迭代对象

# contextlib
# 上下文 with

# XML
# 操作XML两种方法，DOM（读入内存，树结构，比较大）和SAX（流媒体，边读边解析）
# 3个函数， 使用sax解析xml
# start_element end_element char_data
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    
    def end_element(self, name):
        print('sax:end_element:%s' % name)
    
    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser  = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)

# HTMLParser
# 爬虫的时候用得着
from html.parser import HTMLParser
from html.entities import name2codepoint

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>', tag)
    
    def handle_endtag(self, tag):
        print('<%s>',tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        name = chr(name2codepoint[name])
        print('&%s;' % name)

    def handle_charref(self, name):
        if name.startswith('x'):
            name = chr(int(name[1:], 16))
        else:
            name = chr(int(name))
        print('&#%s;' % name)

# parser_html = myHTMLParser()
# parser_html.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')



# 作业，解析出时间 地址 名称


class Python_event_HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for i in attrlist:
                if attrname == i[0]:
                    return i[1]
            return None

        if tag == 'h3' and _attr(attrs,'class') == 'event-title':
            self.in_title = True
        if tag == 'time':
            self.in_time = True
        if  tag == 'span' and _attr(attrs,'class') == 'event-location':
            self.in_location = True
            

    def handle_data(self, data):
        if self.in_title:
            self.event_title.append(data)
            self.in_title = False
        if self.in_time:
            self.event_time.append(data)
            self.in_time = False
        if self.in_location:
            self.event_location.append(data)
            self.in_location = False


    def __init__(self):
        HTMLParser.__init__(self)
        self.event_time = []
        self.event_title = []
        self.event_location = []
        self.in_time = False
        self.in_title = False
        self.in_location = False

if __name__ == '__main__':
    parser_event = Python_event_HTMLParser()
    with open('Events _ Python.org.html') as f:
        htmltext = f.read()
        parser_event.feed(htmltext)
    for i in range(len(parser_event.event_title)):
        print('time %s at location %s, the event %s' % (parser_event.event_time[i], parser_event.event_location[i],     parser_event.event_title[i]))

# urllib
# 请求 get post


