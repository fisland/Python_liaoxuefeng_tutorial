# coding:utf-8

# 异步IO
# 其实就是异步操作，相当于iOS GCD操作，放到后台处理，当完成时候回调
# 不过这里是，一个消息循环，在这个消息循环中，主线程不断地重复‘读取消息-处理消息’这一过程

# 协程
# 又被称为微线程，纤程 英文名 Coroutine
# 优势
# 1. 极高的执行效率。不是线程切换，而是有程序自身控制，没有线程切换的开销。
# 2. 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好
# 因为协程是一个线程执行，如何利用多核CPU，最简单就是多进程+协程

# 通过generator
'''
def consumer():
    r = ''
    print("Generator First Start")
    while True:
        n = yield r
        print("Generator yield Each Setup")
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
        a = 'Hello world' #返回值与a无关

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consuming return %s...' % r)
    c.close()

c = consumer()
produce(c)
'''
import asyncio 
import threading
'''
@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % threading.current_thread())
    r = yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.current_thread())

loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
'''
@asyncio.coroutine
def wget(host):
    print('wget %s....' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))

    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
# async \ await 代替 @asyncio.coroutine 和 yield from 
'''
async def wget(host):
    print('wget %s....' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))

    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
# aiohttp 基于asyncio实现的HTTP框架 web服务器 由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。

'''需求
    编写一个HTTP服务器，分别处理以下URL：
    / - 首页返回b'<h1>Index</h1>'；
    /hello/{name} - 根据URL参数返回文本hello, %s!。
'''

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')
    
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
