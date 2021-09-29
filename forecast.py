import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# def weather_request():
#     url = 'https://wttr.in/Sochi'
#     weather_parameters = {
#         'format': 2,
#         '0': '',
#         'T': '',
#         'M': '',
#         'lang': 'ru'
#     }
#     forecast = f'Weather forecast: {requests.get(url, params=weather_parameters).text}'
#     print(forecast)
#     return forecast
