# 实现目标：在 9000 端口监听 HTTP 请求，并且对首页 / 进行响应
import logging
import asyncio
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    # 注意，必须加上content_type='text/html'才能将接收到的代码解析并显示出来，否则只能接收而不能显示
    return web.Response(body=b'<h1>Awesome!</h1>', content_type='text/html')

async def init(event_loop):
    app = web.Application(loop=event_loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
