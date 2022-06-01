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
        try:
            async with session.get(url, params=weather_parameters, ssl=False) as response:
                forecast = await response.text() if response.status == 200 else f'Cannot connect to host: {url}'
                # print(f'Weather forecast {forecast} in {city}')
                return forecast

        except Exception as ex:
            print(f"weather_module: {ex}")


async def request():
    task = asyncio.create_task(weather_request())
    await task
    await asyncio.sleep(0.1)


asyncio.run(request())
