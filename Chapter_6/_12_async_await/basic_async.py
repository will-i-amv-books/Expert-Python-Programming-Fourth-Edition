import asyncio


async def async_hello():
    print("hello, world!")


loop = asyncio.get_event_loop()
loop.run_until_complete(async_hello())
loop.close()
