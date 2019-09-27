#!/usr/bin/env python3

import click
import requests
import os


API_KEY = os.environ.get('OPEN_WEATHER_MAP_API_KEY')


def current_weather(location, api_key):
    '''Gets the current weather for inputted city.'''

    url = 'https://api.openweathermap.org/data/2.5/weather'

    payload = {
        'zip': location,
        'appid': api_key,
    }

    response = requests.get(url, params=payload)

    return response.json()['weather'][0]['description']



def current_temp(location, api_key):
    '''Gets the current weather for inputted city.'''

    url = 'https://api.openweathermap.org/data/2.5/weather'

    payload = {
        'zip': location,
        'appid': api_key,
    }

    response = requests.get(url, params=payload)

    return response.json()['main']['temp']



@click.command()
@click.argument('location')
@click.option('--api-key', 
              '-a',
              help='Enter your API key for the OpenWeatherMap API.',
              default=API_KEY,
              )
def main(location, api_key):
    '''Shows you the current weather in a zipcode that you enter. Examples of how
    to enter the zipcode:
    
    1. 94087

    Additionally, you will need an API key 
    from OpenWeatherMap for this tool to work, which you can get by signing up 
    for an account at https://openweathermap.org/'''
    
    weather = current_weather(location, api_key)

    k_temperature = current_temp(location, api_key)
    
    f_temperature = int(1.8 * (k_temperature - 273) + 32)
    
    print(f'The weather in {location} right now: {weather}.')
    print(f'The temperature in {location} right now: {f_temperature} degrees Fahrenheit.')





if __name__ == "__main__":
    
    main()


