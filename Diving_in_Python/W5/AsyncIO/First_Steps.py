import asyncio
from urllib.request import urlopen


# async func before PEP 492 Py3.5
#
# @asyncio.coroutine
# def hello_world():
#     while True:
#         print("Hello, world")
#         yield from asyncio.sleep(1.0)

# async func() since PEP 492 Py3.5
#
# async def hello_world():
#     while True:
#         print("Hello, world")
#         await asyncio.sleep(1.0)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world())
# loop.close()

# asyncio.future, same as concurrent.futures,Future
#
# async def slow_operation(future):
#     await asyncio.sleep(1)
#     future.set_result("Future is done")
#
#
# loop = asyncio.get_event_loop()
# future = asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
#
# loop.run_until_complete(future)
# print(future.result())
# loop.close()

# asyncio.Task run a few coroutines in the same time
#
# async def sleep_task(num):
#     for i in range(5):
#         print(f"process task: {num} iter: {i}")
#         await asyncio.sleep(1)
#     return num
#
# loop = asyncio.get_event_loop()
# task_list = [loop.create_task(sleep_task(i)) for i in range(2)]
# loop.run_until_complete(asyncio.wait(task_list))
#
# loop.run_until_complete(loop.create_task(sleep_task(3)))
# result = loop.run_until_complete(asyncio.gather(sleep_task(10), sleep_task(20)))
# loop.close()
# print(result)

# loop.run_in_executor Run synchronous func() in event_loop
#
def sync_get_url(url):
    return urlopen(url).read()


async def load_url(url, loop=None):
    future = loop.run_in_executor(None, sync_get_url, url)
    response = await future
    print(len(response))


loop = asyncio.get_event_loop()
loop.run_until_complete(load_url('https://google.com', loop=loop))

