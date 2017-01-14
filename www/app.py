# logging模块负责生成日志，可以帮助我们对一个应用程序或库实现灵活的事件日志处理
# logging模块可以记录
import logging
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)


# 响应http请求并返回一个html(的body)
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    # 创建事件循环的Web.Application对象
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv

# 获取事件循环的引用
loop = asyncio.get_event_loop()
# 把需要执行的协程扔到事件循环中执行，实现异步IO，直到运行完毕
loop.run_until_complete(init(loop))
# 无限执行直到被终止(手动停止)
loop.run_forever()
