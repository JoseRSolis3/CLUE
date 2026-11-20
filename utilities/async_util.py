import asyncio

async def timer(seconds:int, repeat:bool=False):
    while True:
        await asyncio.sleep(seconds)
        if not repeat:
            break

def run_async(coro):
    asyncio.run(coro)