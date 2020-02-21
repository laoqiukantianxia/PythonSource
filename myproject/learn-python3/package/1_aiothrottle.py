import asyncio
import aiohttp
import aiothrottle

DOWNLOAD = 'https://dd.dadaxiazai.com/17/167150'

@asyncio.coroutine
def load_file(url):
    response = yield from aiohttp.ClientSession().get(url)

    data = yield from response.read()
    with open("largefile.zip", "wb") as file:
        file.write(data)

    aiohttp.ClientSession().close()
    response.close()

# setup the rate limit to 200 KB/s
aiothrottle.limit_rate(2 * 1024)

# download a large file without blocking bandwidth
loop = asyncio.get_event_loop()
loop.run_until_complete(load_file(DOWNLOAD))

# unset the rate limit
aiothrottle.unlimit_rate()
