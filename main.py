import requests


def weather_request():
    url = 'https://wttr.in/Sochi'
    weather_parameters = {
        'format': 2,
        '0': '',
        'T': '',
        'M': '',
        'lang': 'ru'
    }
    forecast = f'Weather forecast: {requests.get(url, params=weather_parameters).text}'
    print(forecast)
    

if __name__ == '__main__':
    weather_request()
