import asyncio
import aiohttp
import os
import time


url = 'http://challenge.dienekes.com.br/api/numbers?page={}'

results = []

start = time.time()


def get_tasks(session):
    tasks = []
    for i in range(0, 1000):
        tasks.append(session.get(url.format(i), ssl=False))
    return tasks


async def get_nums():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())

    return results
asyncio.run(get_nums())

end = time.time()
total_time = end - start
print("It took {} seconds to make 1000 API calls".format(total_time))
