from pyowm import OWM

API_KEY = '本物のAPIキー'

def fetch_weather(city):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f'{city},JP')
    weather = observation.weather
    status = weather.detailed_status
    temp = weather.temperature('celsiu　s')['temp']
    return status, temp

