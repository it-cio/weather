import aiohttp
import asyncio


async def weather_request():
    async with aiohttp.ClientSession() as session:
        city = 'Sochi'  # Enter the name of your city here
        url = f'https://wttr.in/{city}'
        weather_parameters = {
            'format': 2,
            '0': '',
            'T': '',
            'M': '',
            'lang': 'ru'
        }
        async with session.get(url, params=weather_parameters, ssl=False) as response:
            forecast = await response.text() if response.status == 200 else f'Cannot connect to host: {url}'
            # print(f'Weather forecast {forecast} in {city}')
            return forecast

loop = asyncio.get_event_loop()
loop.run_until_complete(weather_request())
