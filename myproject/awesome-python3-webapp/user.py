import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

#协程不能直接运行，需要把协程加入到事件循环（loop）。asyncio.get_event_loop方法可以创建一个事件循环
loop = asyncio.get_event_loop()
#使用run_until_complete将协程注册到事件循环，并启动事件循环。
loop.run_until_complete(test(loop))
# 永远不退出
loop.run_forever() #loop.close() 执行完关闭

for x in test():
    pass
