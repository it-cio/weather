import aiohttp
import asyncio


async def weather_request():

    async with aiohttp.ClientSession() as session:
        url = 'https://wttr.in/Sochi'
        weather_parameters = {
            'format': 2,
            '0': '',
            'T': '',
            'M': '',
            'lang': 'ru'
        }
        async with session.get(url, params=weather_parameters, ssl=False) as response:
            forecast = await response.text() if response.status == 200 else f'Cannot connect to host: {url}'
            print(forecast)
            return forecast

loop = asyncio.get_event_loop()
loop.run_until_complete(weather_request())
